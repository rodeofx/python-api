# -*- coding: utf-8 -*-
# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sys
from setuptools import setup, find_packages

import package

f = open('README.md')
readme = f.read().strip()

f = open('LICENSE')
license = f.read().strip()

# For python 2.4 support
script_args = sys.argv[1:]
if (sys.version_info[0] <= 2) or (sys.version_info[0] == 2 and sys.version_info[1] <= 5):
    if 'install' in script_args and '--no-compile' not in script_args:
        script_args.append('--no-compile')


setup(
    name='shotgun_api3',
    # The + is part of the python packaging specification. It means it's a local version.
    version='3.1.1' + '+{0}'.format(package._rdoVersion),
    description='Shotgun Python API ',
    long_description=readme,
    author='Shotgun Software, RodeoFX',
    author_email='shotgundev@rodeofx.com',
    url='https://github.com/rodeofx/python-api',
    license=license,
    packages=find_packages(exclude=('tests',)),
    script_args=script_args,
    include_package_data=True,
    package_data={'': ['cacerts.txt']},
    zip_safe=False,
    python_requires='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6',
)
