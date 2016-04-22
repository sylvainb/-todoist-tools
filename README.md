Overview
=========

This packages implements some helpers for the Todoist service : https://todoist.com

Export projets
--------------

Allow to export all projects to a TEXT file, a JSON file or an HTML file.

Todoist creates automatic backup every day and allow to download them, 
but it's only for Premium users !

This script allow to create local backups from a Todoist account, 
using the official Todoist Python API library.

Requirements
============

Tested with Python 3.5

Install

First create and activate a virtualenv:

    virtualenv -p <path-to-python> todoist
    git clone git@github.com:sylvainb/todoist-tools.git
    cd todoist-tools
    pip install -e .

Configure your Todoist credentials (username and password):

    cp src/todoist_tools/config.ini.sample src/todoist_tools/config.ini
    vi src/todoist_tools/config.ini

How to : Export projects
========================

With the command line
---------------------

    cd src/todoist_tools
    python export_my_projects.py --help
    python export_my_projects.py --dirpath=/tmp --format=txt
    python export_my_projects.py --dirpath=/tmp --format=json
    python export_my_projects.py -d=/tmp -f=html

With the Python interpreter
---------------------------
TODO ython src/todoist_tools/export_my_projects.py


Credits
=======

Sylvain Boureliou [sylvainb] - [Github](https://github.com/sylvainb) - [Website](http://www.boureliou.com)

Source code
===========

[Source code](<https://github.com/sylvainb/todoist-tools>) is hosted on Github.

How to contribute and submit a patch ?
======================================

[Source code](<https://github.com/sylvainb/todoist-tools>) and an [issue tracker](<https://github.com/sylvainb/todoist-tools/issues>) is hosted on Github.
