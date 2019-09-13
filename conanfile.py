from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools

class ffnvcodecConan(ConanFile):
    name = "ffnvcodec"
    version = "9.0.18.1"
    description = "nv-codec-headers for ffmpeg https://github.com/FFmpeg/nv-codec-headers"
    url = "https://github.com/omaralvarez/conan-ffnvcodec"
    repo_url = "https://github.com/FFmpeg/nv-codec-headers"
    topics = ("c", "header-only")
    generators = "cmake"
    no_copy_source = True

    def source(self):
        self.run("git clone -b 'n%s' --single-branch --depth 1 %s" % (self.version, self.repo_url))
    
    def package(self):
        self.copy("*.h", dst="include", keep_path=False)

    def package_id(self):
        self.info.header_only()
