#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from opps import goalserve


install_requires = ["opps"]

classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Framework :: Opps",
               'Programming Language :: Python',
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
               'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.md').read()
except:
    long_description = goalserve.__description__

setup(
    name='opps-goalserve',
    namespace_packages=['opps', 'opps.goalserve'],
    version=goalserve.__version__,
    description=goalserve.__description__,
    long_description=long_description,
    classifiers=classifiers,
    keywords='goalserve opps cms django apps magazines websites',
    author=goalserve.__author__,
    author_email=goalserve.__email__,
    url='http://oppsproject.org',
    download_url="https://github.com/opps/opps-goalserve/tarball/master",
    license=goalserve.__license__,
    packages=find_packages(exclude=('doc', 'docs',)),
    package_dir={'opps': 'opps'},
    install_requires=install_requires,
)
