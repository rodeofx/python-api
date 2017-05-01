from __future__ import print_function, absolute_import

import os
import os.path
import shutil

packageName = 'shotgun_api3'


def build(source_path, build_path, install_path, targets):

    def _build():
        src = os.path.join(source_path, packageName)
        dest = os.path.join(build_path, packageName)
        shutil.copytree(src, dest)

    def _install(dirName):
        src = os.path.join(build_path, dirName)
        dest = os.path.join(install_path, dirName)
        if os.path.exists(dest):
            print('Found existing local package. Removed.')
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

    def _release():
        """Processes launched at release time."""
        # For legacy purpose, we update the production folder to be linked to the latest version
        # of the package. That allows a smooth transition between rez and old way.
        dest = '/rdo/rodeo/setup/lib/{0}/{0}'.format(packageName)

        if os.path.exists(dest):
            os.unlink(dest)

        src = os.path.join(install_path, packageName)

        print('Install symlink at {0}'.format(dest))

        os.symlink(src, dest)

    _build()
    targets = targets or []

    if "install" in targets:
        _install(packageName)

    elif 'release' in targets:
        _release()
