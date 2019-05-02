from conans import ConanFile, CMake
import os


class LinuxdeploypluginqtConan(ConanFile):
    name = "linuxdeploy-plugin-appimage"
    version = "continuous"
    license = "MIT"
    author = "Alexis Lopez Zubieta contact@azubieta.net"
    url = "https://github.com/appimage-conan-community/linuxdeploy-plugin-appimage_installer"
    description = "linuxdeploy plugin to generate AppImages from AppDirs"
    topics = ("AppImage", "linuxdeploy", "pluggin")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"

    requires = ("appimagetool_installer/11@appimage-conan-community/stable")
    build_requires = ("cmake_installer/3.13.0@conan/stable")

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

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def deploy(self):
        self.copy("*", dst="bin", src="bin")
