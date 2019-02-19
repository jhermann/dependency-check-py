# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.
"""
from __future__ import absolute_import, unicode_literals

import subprocess

from rituals import config
from rituals.easy import *  # pylint: disable=redefined-builtin

config.set_flat_layout()

@task(pre=[clean])  # pylint: disable=undefined-variable
def selfcheck(ctx):
    """Perform integration tests."""
    project = subprocess.check_output('python ./setup.py --name'.split()).strip()
    ctx.run("dependency-check --disableAssembly -s . -o build --project '{}'".format(project))

namespace.add_task(selfcheck)
