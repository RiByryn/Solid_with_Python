#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="python_solid",
    version="0.0.1",
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
