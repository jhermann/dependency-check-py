# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""
from __future__ import absolute_import, unicode_literals

from rituals import config
from rituals.easy import *  # pylint: disable=redefined-builtin

config.set_flat_layout()

@task(pre=[clean])  # pylint: disable=undefined-variable
def selfcheck(ctx):
    """Perform integration tests."""
    ctx.run("dependency-check .")

namespace.add_task(selfcheck)
