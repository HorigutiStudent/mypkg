#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'earthquake_info'
submodules = 'earthquake_info/handlers'

setup(
    name=package_name,
    version='0.0.0',
    # packages=find_packages(exclude=['test']),
    packages=[package_name,submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='horiguti',
    maintainer_email='s23c1127lc@s.chibakoudai.jp',
    description='a package for practice',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'get_info = earthquake_info.get_info:main',
            'listener = earthquake_info.listener:main',
        ],
    },
)
