from conans import ConanFile, CMake, tools
import shutil

class TinyxmlConan(ConanFile):
    name = "tinyxml"
    version = "2.6.2"
    license = "Zlib"
    url = "https://github.com/joakimono/conan-tinyxml"
    homepage = "http://www.grinninglizard.com/tinyxml/"
    description = "<Description of Tinyxml here>"
    settings = "os", "compiler", "build_type", "arch", "os_build", "arch_build"
    generators = "cmake"
    exports = "CMakeLists.txt" , "LICENSE"
    source_file = "tinyxml_2_6_2.tar.gz"
    source_dir =  "tinyxml"
    
    def source(self):
    
        link = "https://sourceforge.net/projects/tinyxml/files/tinyxml/" \
        + self.version + "/" + self.source_file
        tools.get(link, sha1="cba3f50dd657cb1434674a03b21394df9913d764")
        shutil.move("CMakeLists.txt", self.source_dir + "/CMakeLists.txt")
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_dir)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("lib_license/LICENSE", dst="licenses", src=self.source_dir,
                  ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tinyxml"]
        if self.settings.build_type == "Debug":
            self.cpp_info.libs[0] += "_d"