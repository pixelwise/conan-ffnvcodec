project(PackageTest CXX)
cmake_minimum_required(VERSION 3.7)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example main.cpp)
target_link_libraries(example ${CONAN_LIBS})