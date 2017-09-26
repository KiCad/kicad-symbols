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

# Output libraries
output_libs = {}

unallocated_symbols = []
overallocated_symbols = []

# Iterate through all remaining libraries
for src_lib in src_libs:

    lib_name = src_lib.split(os.path.sep)[-1].replace('.lib', '')

    lib = schlib.SchLib(src_lib)

    # Make a copy of each component (so list indexing doesn't get messed up)
    components = [c for c in lib.components]

    # Should this entire library be copied?
    copy_lib = get_entire_lib_match(lib_name)

    if copy_lib is not None:
        if not args.silent:
            print("Copying entire library '{src}' -> '{dst}'".format(src=lib_name, dst=copy_lib))
        if not copy_lib in output_libs:
            output_libs[copy_lib] = schlib.SchLib(os.path.join(dst_dir, copy_lib + '.lib'), create=real_mode)

        out_lib = output_libs[copy_lib]

        for cmp in lib.components:
            out_lib.addComponent(cmp)

        # Skip any further checks
        continue

    for cmp in lib.components:

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
            if not args.silent:
                print("Creating new library - '{lib}'".format(lib=match))

        out_lib = output_libs[match]
        out_lib.addComponent(cmp)

        if not args.silent:
            print("{lib} : {name} -> {out}".format(lib=lib_name, name=cmp.name, out=match))


# Save the converted libraries
for key in output_libs:
    lib = output_libs[key]

    if real_mode:
        lib.save()

if len(unallocated_symbols) > 0:
    print("\nUnallocated Symbols:")
    for s in unallocated_symbols:
        print(s)

if len(overallocated_symbols) > 0:
    print("\nOverallocated Symbols:")
    for s in overallocated_symbols:
        print(s)

remaining = len(unallocated_symbols) + len(overallocated_symbols)

print("")
if remaining > 0:
    print("Symbols remaining: {x}".format(x=remaining))
else:
    print("No symbols remaining! You did well.")
