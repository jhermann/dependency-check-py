#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
    dependency-check - Shim to easily install OWASP dependency-check-cli into Python projects.

    Copyright ©  2015 Jürgen Hermann <jh@web.de>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import io
import os
import re
import sys

project = dict(
    name='dependency-check',
    url='https://github.com/jhermann/dependency-check-py',
    license="Apache 2.0",

    install_requires=[],

    entry_points={
        "console_scripts": [
            "dependency-check = dependency_check:run",
        ],
    }
)

classifiers="""
# Details at http://pypi.python.org/pypi?:action=list_classifiers
Development Status :: 3 - Alpha
#Development Status :: 4 - Beta
#Development Status :: 5 - Production/Stable
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Topic :: Security
Topic :: Software Development :: Quality Assurance
Topic :: Utilities
"""

# Import setuptools
try:
    from setuptools import setup
except ImportError as exc:
    raise RuntimeError("Cannot install '{0}', setuptools is missing ({1})".format(project['name'], exc))

project_root = os.path.abspath(os.path.dirname(__file__))
script_name = os.path.join(project_root, project['name'].replace('-', '_') + '.py')
expected_keys = "version author author_email".split()
with io.open(script_name, encoding='utf-8') as handle:
    for line in handle:
        match = re.match(r"""^__({})__ += (?P<q>['"])(.+?)(?P=q)$""".format('|'.join(expected_keys)), line)
        if match:
            project[match.group(1)] = match.group(3)

project.update(dict(
    py_modules=[project['name'].replace('-', '_')],
    description=__doc__.split('.')[0].split(' - ', 1)[1].strip(),
    long_description=io.open('README.rst', encoding='UTF-8').read().split('\n.. _setup-start:', 1)[-1].strip(),
    classifiers=[i.strip() for i in classifiers.splitlines() if i.strip() and not i.strip().startswith('#')],
))

# Ensure 'setup.py' is importable by other tools, to access the project's metadata
__all__ = ['project', 'project_root']
if __name__ == '__main__':
    if '--metadata' in sys.argv[:2]:
        import json
        json.dump(project, sys.stdout, default=repr, indent=4, sort_keys=True)
        sys.stdout.write('\n')
    else:
        setup(**project)
