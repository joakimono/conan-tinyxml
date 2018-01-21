cmake_minimum_required(VERSION 3.1.2)
project(TinyxmlTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(xmltest xmltest.cpp)
target_link_libraries(xmltest CONAN_PKG::tinyxml)

if(MSVC)
  target_compile_definitions(xmltest PRIVATE -D_CRT_SECURE_NO_WARNINGS) # strcpy, fopen
endif()

enable_testing()
add_test(NAME xmltest
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND xmltest)
