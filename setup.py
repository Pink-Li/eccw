#!/usr/bin/env python3
# -*-coding:utf-8 -*

from setuptools import setup, find_packages
import sys
from distutils.command.install_data import install_data
import subprocess
import os.path as osp


def get_data_files():
    """Return data_files in a platform dependent manner"""
    if sys.platform.startswith('linux'):
        data_files = [('share/applications', ['scripts/eccw.desktop']),
                      ('share/pixmaps', ['eccw/images/icon_eccw_256x256.png']),
                      ('share/metainfo', ['scripts/eccw.appdata.xml'])]
    else:
        data_files = []
    return data_files


# Make Linux detect Spyder desktop file
class MyInstallData(install_data):
    def run(self):
        install_data.run(self)
        if sys.platform.startswith('linux'):
            try:
                subprocess.call(['update-desktop-database'])
            except:
                print("ERROR: unable to update desktop database",
                      file=sys.stderr)
CMDCLASS = {'install_data': MyInstallData}

setup(
    data_files=get_data_files(),
    script=[osp.join('scripts', 'eccw')],
    entry_points={
        'console_scripts': [
            'eccw=eccw.main:launch',
            ],
        },
    # Auto scanning package
    packages=find_packages(),
    # Use MANIFEST.in for custom packaging
    include_package_data=True,
    cmdclass=CMDCLASS,
    )
