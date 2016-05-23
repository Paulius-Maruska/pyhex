#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="pyhex",
    version="0.3.0",
    description="Python Hexadecimal Converter and Viewer",
    classifiers=[
        # project state
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",

        # project information
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    author=u"Paulius Maruška",
    author_email="paulius.maruska+pyhex@gmail.com",
    url="https://github.com/Paulius-Maruska/pyhex",
    license="MIT",
    platforms=["Any"],
    packages=["pyhex"],
    scripts=["pyhexview.py"],
)
