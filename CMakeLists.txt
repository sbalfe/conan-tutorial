cmake_minimum_required(VERSION 3.5)
project(conan_tutorial CXX)

find_package(spdlog REQUIRED)

add_executable(conan_tutorial src/main.cpp)

target_link_libraries(conan_tutorial spdlog::spdlog)