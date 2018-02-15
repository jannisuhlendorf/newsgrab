#!/usr/bin/env python
from setuptools import setup

setup(
    name='newsgrab',
    version='0.0.0',
    author='Jannis Uhlendorf',
    include_package_data=True,
    entry_points={
        "console_scripts": [
            'newsgrab = newsgrab.service:main'
        ]
    }
)