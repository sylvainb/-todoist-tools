#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0dev'

description = \
    "This packages implements some helpers for the Todoist service : https://todoist.com " \
    "(export projects to txt/json/html files)."
long_description = open("README.md").read() + "\n" \
    + open(os.path.join("docs", "HISTORY.md")).read()

setup(name='todoist_tools',
      version=version,
      description=description,
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='python todoist',
      author='Sylvain Boureliou [sylvainb]',
      author_email='sylvain.boureliou@gmail.com',
      url='https://github.com/sylvainb/todoist_tools',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'todoist-python',
          'Jinja2',
      ],
      entry_points={
      }
      )
