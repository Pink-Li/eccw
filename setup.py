#!/usr/bin/env python3
# -*-coding:utf-8 -*

from setuptools import setup, find_packages
#import sys
#from distutils.command.install_data import install_data
#import subprocess
#import os.path as osp


#def get_data_files():
#    """Return data_files in a platform dependent manner"""
#    if sys.platform.startswith('linux'):
#        data_files = [('share/applications', ['scripts/eccw.desktop']),
#                      ('share/pixmaps', [
#                        'eccw/images/icon_eccw_16x16.png',
#                        'eccw/images/icon_eccw_24x24.png',
#                        'eccw/images/icon_eccw_32x32.png',
#                        'eccw/images/icon_eccw_48x48.png',
#                        'eccw/images/icon_eccw_128x128.png',
#                        'eccw/images/icon_eccw_256x256.png',
#                        'eccw/images/icon_eccw_512x512.png'
#                        ]),
#                      ('share/metainfo', ['scripts/eccw.appdata.xml'])]
#    else:
#        data_files = []
#    return data_files


## Make Linux detect ECCW desktop file
#class MyInstallData(install_data):
#    def run(self):
#        install_data.run(self)
#        if sys.platform.startswith('linux'):
#            try:
#                subprocess.call(['update-desktop-database'])
#            except:
#                print("ERROR: unable to update desktop database",
#                      file=sys.stderr)
#CMDCLASS = {'install_data': MyInstallData}


setup(
    entry_points={
        'console_scripts': [
            'eccw=eccw.main:launch',
            ],
        'gui_scripts': [
            'eccw=eccw.main:launch',
            ]
        },
    # Auto scanning package
#    packages=find_packages(),
    # Use MANIFEST.in for custom packaging
#    include_package_data=True,

#    install_requires = [
#        'numpy>=1.10',
#        'matplotlib>=2.0',
#        'pyqt5>=5.6',
#        'xmltodict>=0.10',
#        ],
#    python_requires = '>=3.3',

#    data_files=get_data_files(),
#    scripts=[osp.join('scripts', 'eccw/bin/eccw')],
#    cmdclass=CMDCLASS,
    )
