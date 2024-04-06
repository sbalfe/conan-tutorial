from conan import ConanFile

class ConanTutorialRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    generators = ["CMakeDeps","CMakeToolchain"]

    def requirements(self):
        self.requires("spdlog/1.13.0")


    