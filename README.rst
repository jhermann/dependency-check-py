dependency-check
================

 |Travis CI|  |GitHub Issues|  |License|
 |Development Status|  |Latest Version|  |Download format|  |Downloads|


Shim to easily install OWASP dependency-check-cli into Python projects.

.. _setup-start:

Usage
-----

Installation
------------

*dependency-check* can be installed via ``pip install dependency-check`` as usual,
see `releases <https://github.com/jhermann/dependency-check-py/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="jhermann/dependency-check-py"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=dependency-check"

As a developer, to create a working directory for this project, call these commands::

    git clone "https://github.com/jhermann/dependency-check-py.git"
    cd "dependency-check-py"
    . .env --yes --develop
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.org/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


.. |Travis CI| image:: https://api.travis-ci.org/jhermann/dependency-check-py.svg
    :target: https://travis-ci.org/jhermann/dependency-check-py
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/dependency-check-py.svg
    :target: https://coveralls.io/r/jhermann/dependency-check-py
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/dependency-check-py.svg
    :target: https://github.com/jhermann/dependency-check-py/issues
.. |License| image:: https://img.shields.io/pypi/l/{{ cookiecutter.repos_name }}.svg
    :target: https://github.com/jhermann/dependency-check-py/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/dependency-check/badge.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Latest Version| image:: https://img.shields.io/pypi/v/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Download format| image:: https://pypip.in/format/dependency-check/badge.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Downloads| image:: https://img.shields.io/pypi/dw/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
