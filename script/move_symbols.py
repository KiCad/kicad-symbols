from __future__ import print_function

import shutil
import os
import argparse
import fnmatch
import sys
import glob

from lib_patterns import *

parser = argparse.ArgumentParser(description='Reorganizing the KiCad libs is fun!')
parser.add_argument('libs', help='List of source libraries', nargs='+')
parser.add_argument('dest_dir', help='Path to store the output')
parser.add_argument('--schlib', help='Path to schlib scripts', action='store')
parser.add_argument('--real', help='Real run (test run by default)', action='store_true')
parser.add_argument('--required', help='Add list of required library names even if empty', action='store_true')
parser.add_argument('--silent', help='Suppress output messages', action='store_true')
args = parser.parse_args()

real_mode = args.real

if args.schlib:
    sys.path.append(os.path.abspath(args.schlib))

# Import the schlib utils
import schlib

dst_dir = os.path.abspath(args.dest_dir)

# Output dir must exist if real output is to be made
if not os.path.isdir(dst_dir) and args.real:
    print("dest_dir not a valid directory")
    sys.exit(1)

# Find the source libraries
src_libs = []
for lib in args.libs:
    src_libs += glob.glob(lib)

# Rename a library
def rename_lib(src_lib, dst_lib):
    dst_file = os.path.join(dst_dir, dst_lib)

    # Move the .lib file
    shutil.copyfile(src_lib, dst_file + '.lib')

    # Move the dst file
    shutil.copyfile(src_lib.replace('.lib', '.dcm'), dst_file + '.dcm')


# Find any libraries that just have to be copied,
# keep track of any other patterns

for p in PATTERNS:

    lib_name = get_lib_name(p)
    part_filter = get_part_filter(p)
    output_lib = PATTERNS[p]

    lib_src = lib_name + '.lib'

    lib_src_file = None

    # Find the library to move
    for lib in src_libs:
        if lib_src in lib:
            lib_src_file = lib
            break

    if is_entire_lib(p):
        if not lib_src_file:
            continue
        if not args.silent:
            print('Moving {src} -> {dst}'.format(src=lib_name, dst=output_lib))

        if real_mode:
            rename_lib(lib_src_file, output_lib)

        src_libs.remove(lib_src_file)

# Dict of libs to write to
output_libs = {}

unallocated_symbols = []
overallocated_symbols = []

# Iterate through all remaining libraries
for src_lib in src_libs:

    lib_name = src_lib.split(os.path.sep)[-1].replace('.lib', '')

    lib = schlib.SchLib(src_lib)

    # Make a copy of each component (so list indexing doesn't get messed up)
    components = [c for c in lib.components]

    for cmp in components:

        # A component should not match more than one filter
        filter_matches = 0

        matches = get_matches(lib_name, cmp.name)

        # No matches found
        if len(matches) == 0:
            unallocated_symbols.append(lib_name + ' : ' + cmp.name)
            continue

        # Too many matches!
        if len(matches) > 1:
            overallocated_symbols.append(lib_name + ' : ' + cmp.name)
            continue

        match = matches[0]

        # Is there already an output library made?
        if not match in output_libs:
            output_lib_name = os.path.join(dst_dir, match + '.lib')
            output_libs[match] = schlib.SchLib(output_lib_name, create=real_mode)

        out_lib = output_libs[match]

        out_lib.addComponent(cmp)

# Ensure that all the REQUIRED_LIBS are added
if args.required:
    for lib in REQUIRED_LIBS:
        if not lib in output_libs:
            fn = os.path.join(dst_dir, lib + '.lib')
            output_libs[lib] = schlib.SchLib(fn, create=real_mode)
            if not args.silent:
                print("Adding empty library - " + lib)

# Save the converted libraries
for key in output_libs:
    lib = output_libs[key]

    if real_mode:
        lib.save()

if not args.silent and len(unallocated_symbols) > 0:
    print("Unallocated Symbols:")
    for s in unallocated_symbols:
        print(s)

if not args.silent and len(overallocated_symbols) > 0:
    print("Overallocated Symbols:")
    for s in overallocated_symbols:
        print(s)

remaining = len(unallocated_symbols) + len(overallocated_symbols)

print("")
if remaining > 0:
    print("Symbols remaining: {x}".format(x=remaining))
else:
    print("No symbols remaining! You did well.")
