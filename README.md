[![Download](https://api.bintray.com/packages/joakimono/conan/tinyxml%3Ajoakimono/images/download.svg)](https://bintray.com/joakimono/conan/tinyxml%3Ajoakimono/_latestVersion)
[![Build Status UNIX](https://travis-ci.org/joakimono/conan-tinyxml.png?branch=master)](https://travis-ci.org/joakimono/conan-tinyxml)
[![Build Status WIND](https://ci.appveyor.com/api/projects/status/github/joakimono/conan-tinyxml?branch=master&svg=true)](https://ci.appveyor.com/project/joakimono/conan-tinyxml)


[Conan.io](https://conan.io) recipe for [tinyxml](http://www.grinninglizard.com/tinyxml).

The recipe generates library packages, which can be found at [Bintray](https://bintray.com/joakimono/conan/tinyxml%3Ajoakimono).
The package is usually consumed using the `conan install` command or a *conanfile.txt*.

## How to use this package

1. Add remote to conan's package [registry.txt](http://docs.conan.io/en/latest/reference/config_files/registry.txt.html):

   ```bash
   $ conan remote add joakimono https://api.bintray.com/conan/joakimono/conan
   ```

2. Using *conanfile.txt* in your project with *cmake*

   Add a [*conanfile.txt*](http://docs.conan.io/en/latest/reference/conanfile_txt.html) to your project. This file describes dependencies and your configuration of choice, e.g.:

   ```
   [requires]
   tinyxml/[>=2.6.2]@joakimono/stable

   [options]


   [imports]
   licenses, * -> ./licenses @ folder=True

   [generators]
   cmake
   ```

   Insert into your *CMakeLists.txt* something like the following lines:
   ```cmake
   cmake_minimum_required(VERSION 3.1.2)
   project(TheProject CXX)

   include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
   conan_basic_setup(TARGETS)

   add_executable(the_executor code.cpp)
   target_link_libraries(the_executor CONAN_PKG::tinyxml)
   ```
   Then, do
   ```bash
   $ mkdir build && cd build
   $ conan install ..
   ```
   You can now continue with the usual dance with cmake commands for configuration and compilation. For details on how to use conan, please consult [Conan.io docs](http://docs.conan.io/en/latest/)

## Package options

None

## Known recipe issues

Not tested for mingw or cygwin on Windows.
