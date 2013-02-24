#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Paulius Maruška
from setuptools import setup

setup(name='pyhex',
      version='0.2.0',
      description='Python Hexadecimal Converter and Viewer',
      long_description='Python Hexadecimal Converter and Viewer',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'],
      author=u'Paulius Maruška',
      author_email='paulius.maruska@gmail.com',
      url='https://github.com/Paulius-Maruska/pyhex',
      license='MIT',
      platforms=['Any'],
      packages=['pyhex'],
      scripts=['pyhexview.py'])
