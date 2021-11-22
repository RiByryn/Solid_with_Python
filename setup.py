#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)

setup(
    name="pysolid",
    version=get_property('__version__', "src\pysolid"),
    description="Test module for creating part in SolidWorks from python",
    author="Mary Antonovich",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["openpyxl", "pypiwin32", "pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9"
)
