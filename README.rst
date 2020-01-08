dependency-check
================

 |Travis CI|  |GitHub Issues|  |License|  |Latest Version|


Shim to easily install the `OWASP dependency-check-cli`_ tool into Python projects.

.. contents:: **Table of Contents**

.. _setup-start:

Overview
--------

``dependency-check`` scans application dependencies and checks whether they contain any published vulnerabilities
(based on the NIST `NVD`_).
It runs in the JVM, so you need some form of ``java`` available in your ``PATH``.
The script should work on Linux, Mac OSX and Windows, but right now is only tested on Linux.


Usage
-----

After installation, you'll have the ``dependency-check`` command available that, on first use,
will automatically download and install the OWASP release archive once for all projects.
It'll then redirect any calls to that installation, meaning the downloaded NVD data is shared
amongst projects.

.. code-block::

    dependency-check --disableAssembly -s . -o build --project "$(python ./setup.py --name)" \
        && xdg-open build/dependency-check-report.html

Please see the `DependencyCheck site`_ for more configuration and usage details.

To install from PyPI, add ``dependency-check`` to your ``dev-requirements.txt``
or a similar file. For more installation options, see the next section.

To just get the ``dependency-check`` CLI tool installed into your home,
independent of any project, you can use the `pip script installer`_ or
``pip install --user dependency-check``.

 |Installation Demo|


Customization
-------------

Using environment variables, you can change the version and download location of the release archive,
and the directory for the local installation.

=============================== ==============================================================================================
Variable                        Default
=============================== ==============================================================================================
``DEPENDENCY_CHECK_VERSION``    ``5.2.4``
``DEPENDENCY_CHECK_URL``        ``https://bintray.com/artifact/download/jeremy-long/owasp/dependency-check-{version}-release.zip``
``DEPENDENCY_CHECK_HOME``       ``~/.local/dependency-check``
``DEPENDENCY_CHECK_NVD_URL``    *Use NIST NVD URLs*
=============================== ==============================================================================================

To update to a new version of the OWASP software,
delete ``~/.local/dependency-check/bin/``,
set ``DEPENDENCY_CHECK_VERSION`` to the new version number,
and call ``dependency-check``.

The variable ``DEPENDENCY_CHECK_NVD_URL`` can be used to point to a local copy of the various NVD feeds,
in a flat hierarchy with compressed JSON files.

.. code-block:: shell

    export DEPENDENCY_CHECK_NVD_URL='https://repo.local/nvd/nvdcve-1.0-%d.json.gz

If you set this, the options ``--cveUrlBase`` and ``--cveUrlModified`` will be added to each call.
Note that the ``%d`` representing the year is replaced by ``modified`` for the latter.

Remove the ``~/.local/dependency-check/data/`` directory to force a full data reload.


Installation
------------

*dependency-check* can be installed via ``pip install dependency-check`` as usual,
see `releases <https://github.com/jhermann/dependency-check-py/releases>`_ for an overview of available versions.
To get a bleeding-edge version from source, use these commands::

    repo="jhermann/dependency-check-py"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -U -e "git+https://github.com/$repo.git#egg=dependency-check"

As a developer, to create a working directory for this project, call these commands::

    git clone "https://github.com/jhermann/dependency-check-py.git"
    cd "dependency-check-py"
    . .env --yes --develop
    invoke build check

You might also need to follow some
`setup procedures <https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup>`_
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.


Other Python Security Tools
---------------------------

* `openstack/bandit`_ – Security linter designed to find common security issues in Python code, by static AST analysis.
* `pyupio/safety`_ – Safety checks your installed dependencies for known security vulnerabilities.

  * `pyupio/safety-db`_ – A curated database of security vulnerabilities in Python packages.

* `eliasgranderubio/dagda`_ – Static analysis of known vulnerabilities, trojans, viruses, malware & other malicious threats in Docker images, and runtime monitoring of containers for anomalous activities.
* `anchore/anchore-engine`_ – A service for inspection, analysis and certification of container images, provided as a ready-to-deploy Docker container image.

* `vintasoftware/python-linters-and-code-analysis`_ – Curated list of Python linters and code analysis tools.


.. _`openstack/bandit`: https://github.com/openstack/bandit
.. _`pyupio/safety`: https://github.com/pyupio/safety
.. _`pyupio/safety-db`: https://github.com/pyupio/safety-db
.. _`eliasgranderubio/dagda`: https://github.com/eliasgranderubio/dagda
.. _`anchore/anchore-engine`: https://github.com/anchore/anchore-engine
.. _`vintasoftware/python-linters-and-code-analysis`: https://github.com/vintasoftware/python-linters-and-code-analysis

.. _`NVD`: https://nvd.nist.gov/
.. _`OWASP dependency-check-cli`: https://github.com/jeremylong/dependencycheck#dependency-check
.. _`DependencyCheck site`: https://www.owasp.org/index.php/OWASP_Dependency_Check
.. _`pip script installer`: https://github.com/mitsuhiko/pipsi#pipsi

.. |Installation Demo| image:: https://raw.githubusercontent.com/jhermann/dependency-check-py/master/dependency_check.gif

.. |Travis CI| image:: https://api.travis-ci.org/jhermann/dependency-check-py.svg
    :target: https://travis-ci.org/jhermann/dependency-check-py
.. |Coveralls| image:: https://img.shields.io/coveralls/jhermann/dependency-check-py.svg
    :target: https://coveralls.io/r/jhermann/dependency-check-py
.. |GitHub Issues| image:: https://img.shields.io/github/issues/jhermann/dependency-check-py.svg
    :target: https://github.com/jhermann/dependency-check-py/issues
.. |License| image:: https://img.shields.io/pypi/l/dependency-check.svg
    :target: https://github.com/jhermann/dependency-check-py/blob/master/LICENSE
.. |Development Status| image:: https://img.shields.io/pypi/status/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Latest Version| image:: https://img.shields.io/pypi/v/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Download format| image:: https://img.shields.io/pypi/format/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
.. |Downloads| image:: https://img.shields.io/pypi/dw/dependency-check.svg
    :target: https://pypi.python.org/pypi/dependency-check/
