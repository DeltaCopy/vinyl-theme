cmake_minimum_required(VERSION 3.16)

if( CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR )
project(vinyl-icons)
else()
# We are building as part of Main project
endif()

find_package(ECM ${KF6_MIN_VERSION} REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${ECM_MODULE_PATH}  ${CMAKE_SOURCE_DIR}/cmake)

find_package(Qt6 ${QT_MIN_VERSION} REQUIRED CONFIG COMPONENTS Core)
include(KDEInstallDirs6)

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/build/Vinyl
  COMMAND sh ${CMAKE_CURRENT_SOURCE_DIR}/make-theme.sh
)

add_custom_target(icon-themes ALL
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/build/Vinyl
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/build/Vinyl/
  DESTINATION ${KDE_INSTALL_DATADIR}/icons/Vinyl/
)
