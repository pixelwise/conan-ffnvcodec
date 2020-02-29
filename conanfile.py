from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools
import re
VERSION_REGEX = re.compile(r'([0-9.]+)-(.+)-([a-z0-9]+)')

def parse_version(version: str):
    matches = VERSION_REGEX.match(version)
    if matches:
        return matches.groups()
    raise RuntimeError('% does not match version pattern: %s'%version%VERSION_REGEX.pattern)


class ffnvcodecConan(ConanFile):
    name = "ffnvcodec"
    description = "nv-codec-headers for ffmpeg https://github.com/maddanio/nv-codec-headers.git"
    url = "https://github.com/pixelwise/conan-ffnvcodec"
    repo_url = "https://github.com/maddanio/nv-codec-headers.git"
    topics = ("c", "header-only")
    generators = "cmake"
    no_copy_source = True

    def source(self):
        _target_version, self.repo_branch, self.target_commit = parse_version(self.version)
        git = tools.Git()
        git.clone(
            self.repo_url,
            branch=self.repo_branch,
            shallow=True,
        )
        current_commit = git.get_commit()
        if not current_commit.startswith(self.target_commit):
            # if the wanted commit is not on the top
            # we have to get full repo
            git.run('fetch --unshallow')
            if self.target_commit:
                git.checkout(self.target_commit)

    def package(self):
        self.copy("*.h", dst="include/ffnvcodec", keep_path=False)

    def package_id(self):
        self.info.header_only()
