from conans import ConanFile, CMake


class LinuxdeploypluginqtConan(ConanFile):
    name = "linuxdeploy-plugin-appimage"
    version = "continuous"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Linuxdeploypluginqt here>"
    topics = ("AppImage", "linuxdeploy", "plugin")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"
    exports_sources = "src/*"

    def source(self):
        self.run("git clone https://github.com/linuxdeploy/linuxdeploy-plugin-appimage.git --depth=1")
        self.run("cd linuxdeploy-plugin-appimage && git submodule update --init --recursive")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["USE_CCACHE"] = False
        cmake.configure(source_folder="linuxdeploy-plugin-appimage")
        cmake.build()

    def package(self):
        self.copy("*linuxdeploy-plugin-appimage", dst="bin", src="src")

    def deploy(self):
        self.copy("*", dst="bin", src="bin")
