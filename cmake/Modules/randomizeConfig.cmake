INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RANDOMIZE randomize)

FIND_PATH(
    RANDOMIZE_INCLUDE_DIRS
    NAMES randomize/api.h
    HINTS $ENV{RANDOMIZE_DIR}/include
        ${PC_RANDOMIZE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RANDOMIZE_LIBRARIES
    NAMES gnuradio-randomize
    HINTS $ENV{RANDOMIZE_DIR}/lib
        ${PC_RANDOMIZE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RANDOMIZE DEFAULT_MSG RANDOMIZE_LIBRARIES RANDOMIZE_INCLUDE_DIRS)
MARK_AS_ADVANCED(RANDOMIZE_LIBRARIES RANDOMIZE_INCLUDE_DIRS)

