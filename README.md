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
=======

First create and activate a virtualenv:

    virtualenv -p <path-to-python> todoist
    git clone git@github.com:sylvainb/todoist_tools.git
    cd todoist_tools
    pip install -e .

How to : Export projects
========================

With the command line
---------------------

Configure your Todoist credentials (username and password):

    cd todoist_tools
    cp src/todoist_tools/config.ini.sample src/todoist_tools/config.ini
    vi src/todoist_tools/config.ini

Then:

    cd src/todoist_tools
    python projects.py --help
    python projects.py --dirpath=/tmp --format=txt
    python projects.py --dirpath=/tmp --format=json
    python projects.py -d=/tmp -f=html

With the Python interpreter
---------------------------

    from todoist_tools.projects import ProjectsExport
    export = ProjectsExport('todoist_email', 'todoist_password')
    export.to_text('./todoist.txt')
    export.to_json('./todoist.json')
    export.to_html('./todoist.html')

Credits
=======

Sylvain Boureliou [sylvainb] - [Github](https://github.com/sylvainb) - [Website](http://www.boureliou.com)

Source code
===========

[Source code](<https://github.com/sylvainb/todoist_tools>) is hosted on Github.

How to contribute and submit a patch ?
======================================

[Source code](<https://github.com/sylvainb/todoist_tools>) and an [issue tracker](<https://github.com/sylvainb/todoist_tools/issues>) is hosted on Github.
