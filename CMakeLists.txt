project( kicad-symbols NONE )

cmake_minimum_required( VERSION 2.6.1 FATAL_ERROR )

#================================================
# Locations for install targets.
#================================================
if( APPLE )
    # Like all variables, CMAKE_INSTALL_PREFIX can be over-ridden on the command line.
    set( CMAKE_INSTALL_PREFIX "/Library/Application Support/kicad/" CACHE PATH "" )

    # Everything without leading / is relative to CMAKE_INSTALL_PREFIX.
    set( KICAD_LIBRARY library )
    set( KICAD_TEMPLATE template )
else()
    # Everything without leading / is relative to CMAKE_INSTALL_PREFIX.
    set( KICAD_DATA share/kicad
         CACHE PATH "Location of KiCad data files." )
    set( KICAD_LIBRARY ${KICAD_DATA}/library )
    set( KICAD_TEMPLATE ${KICAD_DATA}/template )
endif()

mark_as_advanced( KICAD_DATA KICAD_LIBRARY )


#================================================
# "make uninstall" rules
#================================================
configure_file(
    "${PROJECT_SOURCE_DIR}/CMakeModules/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
    IMMEDIATE @ONLY )

add_custom_target( uninstall
    "${CMAKE_COMMAND}" -P "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake" )


#================================================
# Installed files.
#================================================

# Install all of the symbol library (.lib) and document (.dcm) files in this folder.
file(GLOB dcm_files "*.dcm")
file(GLOB lib_files "*.lib")

install(FILES ${dcm_files}
        DESTINATION ${KICAD_LIBRARY}
        COMPONENT resources)

install(FILES ${lib_files}
        DESTINATION ${KICAD_LIBRARY}
        COMPONENT resources)

# Install the default global symbol library table in the template folder.
install(FILES sym-lib-table
        DESTINATION ${KICAD_TEMPLATE}
        COMPONENT resources)
