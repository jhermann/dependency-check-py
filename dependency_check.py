# -*- coding: utf-8 -*-
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
from __future__ import absolute_import, unicode_literals, print_function

__version__ = '0.2.0'
__author__ = 'Jürgen Hermann'
__author_email__ = 'jh@web.de'


import os
import sys
import shutil
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import zipfile
import tempfile
import subprocess
from contextlib import closing


DEPENDENCY_CHECK_VERSION = '2.1.1'
DEPENDENCY_CHECK_URL = 'https://bintray.com/artifact/download/jeremy-long/owasp/dependency-check-{version}-release.zip'


def install_path():
    """Return the target path for installation of ``dependency-check-cli``."""
    return os.environ.get('DEPENDENCY_CHECK_HOME', os.path.expanduser('~/.local/dependency-check')).rstrip(os.sep)


def install():
    """Install the ZIP release."""
    dc_home = install_path()
    dc_command = os.path.join(dc_home, 'bin', 'dependency-check' + ('.bat' if sys.platform == 'win32' else '.sh'))

    if not os.path.isfile(dc_command):
        # Install `dependency-check-cli` release
        dc_url = os.environ.get('DEPENDENCY_CHECK_URL', DEPENDENCY_CHECK_URL)
        dc_version = os.environ.get('DEPENDENCY_CHECK_VERSION', DEPENDENCY_CHECK_VERSION)
        dc_url = dc_url.format(version=dc_version)
        install_ok = False

        with tempfile.NamedTemporaryFile(suffix='.zip', prefix='dependency-check-', delete=False) as zip_temp:
            try:
                print("Downloading '{}'...".format(dc_url))
                with closing(urlopen(dc_url)) as url_handle:
                    shutil.copyfileobj(url_handle, zip_temp)
                zip_temp.close()

                print("Unpacking '{}' to '{}'...".format(zip_temp.name, dc_home))
                if not os.path.isdir(dc_home):
                    os.makedirs(dc_home)
                with closing(zipfile.ZipFile(zip_temp.name)) as zip_handle:
                    for member in zip_handle.infolist():  # bogus pylint: disable=no-member
                        out_path = dc_home + os.sep + member.filename.split('/', 1)[1]
                        if member.filename.endswith('/'):
                            if not os.path.isdir(out_path):
                                os.makedirs(out_path)
                        else:
                            with closing(zip_handle.open(member)) as inp:  # bogus pylint: disable=no-member
                                with open(out_path, 'wb') as out:
                                    shutil.copyfileobj(inp, out)
                os.chmod(os.path.join(dc_home, 'bin', 'dependency-check.sh'), 0o755)
                install_ok = True
            finally:
                if not install_ok and os.path.exists(dc_command):
                    os.remove(dc_command)  # mark failed install as incomplete
                if os.path.exists(zip_temp.name):
                    os.remove(zip_temp.name)

    return dc_command


def dc_opts():
    """Return additional options to inject into the dependency-check command."""
    opts = []
    nvd_base_url = os.environ.get('DEPENDENCY_CHECK_NVD_URL', '').rstrip('/')

    if nvd_base_url:
        opts.extend([
            '--cveUrl12Modified', '{}/nvdcve-Modified.xml'.format(nvd_base_url),
            '--cveUrl20Modified', '{}/nvdcve-2.0-Modified.xml'.format(nvd_base_url),
            '--cveUrl12Base', '{}/nvdcve-%d.xml'.format(nvd_base_url),
            '--cveUrl20Base', '{}/nvdcve-2.0-%d.xml'.format(nvd_base_url),
        ])

    return opts


def run():
    """Execute main loop."""
    try:
        # Delegate to `dependency-check-cli`
        dc_command = install()
        sys.exit(subprocess.call([dc_command] + dc_opts() + sys.argv[1:]))
    except KeyboardInterrupt:
        sys.stderr.flush()
        sys.exit(2)


if __name__ == '__main__':
    run()
