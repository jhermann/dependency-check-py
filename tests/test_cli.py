import pytest

import dependency_check


def test_entry_point():
    assert callable(dependency_check.run)
