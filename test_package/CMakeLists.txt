project(TinyxmlTest CXX)
cmake_minimum_required(VERSION 3.1.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(xmltest xmltest.cpp)
target_link_libraries(xmltest ${CONAN_LIBS})

add_definitions(-D_CRT_SECURE_NO_WARNINGS) # strcpy, fopen

enable_testing()
add_test(NAME xmltest
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND xmltest)
