#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import setuptools


def get_classifiers():
    return [
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
    ]


def get_long_description():
    with open('README.rst') as fd:
        return fd.read()


def get_version():
    setup_py_path = os.path.abspath(__file__)
    setup_py_dir = os.path.dirname(setup_py_path)
    pyhex_init_path = os.path.join(setup_py_dir, "pyhex", "__init__.py")
    with open(pyhex_init_path) as f:
        for line in f.readlines():
            if "__version__" in line:
                return line.strip().split("=")[-1].strip(" '\"")
    raise ValueError("could not find version")


def main():
    debug = False
    setup_args = dict(
        name="pyhex",
        version=get_version(),
        description="Python Hexadecimal Converter and Viewer",
        long_description=get_long_description(),
        classifiers=get_classifiers(),
        author=u"Paulius Maruška",
        author_email=u"paulius.maruska+pyhex@gmail.com",
        url=u"https://github.com/Paulius-Maruska/pyhex",
        license="MIT license",
        platforms=["Any"],
        packages=setuptools.find_packages(),
        entry_points={
            "console_scripts": "pyhex = pyhex:main",
        },
    )
    if not debug:
        setuptools.setup(**setup_args)
    else:
        import pprint
        pprint.pprint(setup_args)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
