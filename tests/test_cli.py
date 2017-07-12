import os
import shutil
import tempfile

import pytest

import dependency_check

ENV_NVD_URL = 'DEPENDENCY_CHECK_NVD_URL'

def test_entry_point():
    assert callable(dependency_check.run)


def test_install():
    stage = tempfile.mkdtemp(prefix='dc-test-')
    try:
        os.environ['DEPENDENCY_CHECK_HOME'] = stage
        cmd = dependency_check.install()
        del os.environ['DEPENDENCY_CHECK_HOME']

        assert cmd.endswith('.sh')
    finally:
        shutil.rmtree(stage)


def test_default_options():
    if ENV_NVD_URL in os.environ:
        del os.environ[ENV_NVD_URL]
    options = dependency_check.dc_opts()

    assert not options


def test_options_with_custom_url():
    os.environ[ENV_NVD_URL] = 'http://example.com'
    options = dependency_check.dc_opts()

    assert options[0].startswith('--cveUrl')
    assert options[1].startswith(os.environ[ENV_NVD_URL])
