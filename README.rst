dependency-check
================

.. image:: https://pypip.in/v/dependency-check/badge.png
    :target: https://pypi.python.org/pypi/dependency-check
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/jhermann/dependency-check-py.png
   :target: https://travis-ci.org/jhermann/dependency-check-py
   :alt: Latest Travis CI build status

Shim to easily install OWASP dependency-check-cli into Python projects.

.. _setup-start:

Usage
-----

Installation
------------

*dependency-check* can be installed via ``pip install dependency-check`` as usual,
see `releases <https://github.com/jhermann/dependency-check/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="jhermann/dependency-check"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

As a developer, to create a working directory for this project, call these commands::

    git clone "https://github.com/jhermann/dependency-check.git"
    cd "dependency-check"
    . .env --yes --develop
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.org/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.
