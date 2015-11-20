dependency-check
================

 |Travis CI|  |GitHub Issues|  |License|
 |Development Status|  |Latest Version|  |Download format|  |Downloads|


Shim to easily install the `OWASP dependency-check-cli`_ tool into Python projects.

.. _setup-start:

``dependency-check`` scans application dependencies and checks whether they contain any published vulnerabilities
(based on the NIST `NVD`_).
It runs in the JVM, so you need some form of ``java`` available in your ``PATH``.


Usage
-----

To install from PyPI, add ``dependency-check`` to your ``dev-requirements.txt``
or a similar file. For more installation options, see the next section.

To just get the ``dependency-check`` CLI tool installed into your home,
independant of any project, you can use the `pip script installer`_.

On first use, the release archive is automatically downloaded and installed once,
for all projects. Please see the `DependencyCheck site`_ for more configuration and usage details.


Customization
-------------

Using environment variables, you can change the version and download location of the release archive,
and the directory for the local installation.

=============================== ==============================================================================================
Variable                        Default
=============================== ==============================================================================================
``DEPENDENCY_CHECK_VERSION``    ``1.3.1``
``DEPENDENCY_CHECK_URL``        ``https://bintray.com/artifact/download/jeremy-long/owasp/dependency-check-{version}-release.zip``
``DEPENDENCY_CHECK_HOME``       ``~/.local/dependency-check``
=============================== ==============================================================================================

To update to a new version,
delete ``~/.local/dependency-check/bin/``,
set ``DEPENDENCY_CHECK_VERSION`` to the new version number,
and call ``dependency-check``.


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


.. _`NVD`: https://nvd.nist.gov/
.. _`OWASP dependency-check-cli`: https://github.com/jeremylong/dependencycheck#dependency-check
.. _`DependencyCheck site`: https://www.owasp.org/index.php/OWASP_Dependency_Check
.. _`pip script installer`: https://github.com/mitsuhiko/pipsi#pipsi

.. |Travis CI| image:: https://api.travis-ci.org/jhermann/dependency-check-py.svg
    :target: https://travis-ci.org/jhermann/dependency-check-py
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/dependency-check-py.svg
    :target: https://coveralls.io/r/jhermann/dependency-check-py
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/dependency-check-py.svg
    :target: https://github.com/jhermann/dependency-check-py/issues
.. |License| image:: https://img.shields.io/pypi/l/dependency-check.svg
    :target: https://github.com/jhermann/dependency-check-py/blob/master/LICENSE
.. |Development Status| image:: https://pypip.in/status/dependency-check/badge.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Latest Version| image:: https://img.shields.io/pypi/v/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Download format| image:: https://pypip.in/format/dependency-check/badge.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Downloads| image:: https://img.shields.io/pypi/dw/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
