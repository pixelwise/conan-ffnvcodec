from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools

class ffnvcodecConan(ConanFile):
    name = "ffnvcodec"
    version = "9.0.18.2"
    description = "nv-codec-headers for ffmpeg https://github.com/maddanio/nv-codec-headers.git"
    url = "https://github.com/pixelwise/conan-ffnvcodec"
    repo_url = "https://github.com/maddanio/nv-codec-headers.git"
    topics = ("c", "header-only")
    generators = "cmake"
    no_copy_source = True

    def source(self):
        self.run("git clone -b modules_merged --single-branch --depth 1 %s" % (self.repo_url))

    def package(self):
        self.copy("*.h", dst="include/ffnvcodec", keep_path=False)

    def package_id(self):
        self.info.header_only()
