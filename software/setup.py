#!/usr/bin/env python

import sys
import re

from setuptools import setup, find_packages

def version():
    with open('darwinoppy/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)


extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='darwinoppy',
      version=version(),
      packages=find_packages(),

      install_requires=['pypot >= 2.10', 'poppy-creature'],

      setup_requires=['setuptools_git >= 0.3', ],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Thierry Chantier',
      author_email='titimoby@gmail.com',
      description='Darwinoppy software library for Poppy project',
      url='https://github.com/titimoby/darwinoppy',
      license='GNU GENERAL PUBLIC LICENSE Version 3',
      )
