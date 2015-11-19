# -*- coding: utf-8 -*-
"""
    dependency-check - Shim to easily install OWASP dependency-check-cli into Python projects.
"""
from __future__ import absolute_import, unicode_literals, print_function

__version__ = '0.1.0'
__author__ = 'Jürgen Hermann'
__author_email__ = 'jh@web.de'


import sys
import time
import errno
import codecs
import logging
import argparse


def setup():
    """Set up runtime environment."""
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf8')(sys.stderr)
    logging.basicConfig(level=logging.INFO)


def make_argparser():
    """Create a parser instance for this tool's options."""
    parser = argparse.ArgumentParser(description=__doc__.split('\n    Copyright ', 1)[0])

    parser.add_argument('-V', '--version', action='store_true', default=False,
                        help="show version number and exit")
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help="reduce logging output")
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help="increase logging output")

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    if args.verbose and args.quiet:
        parser.error("Cannot be both quiet and verbose!")
    elif args.quiet:
        logging.getLogger().setLevel(logging.WARNING)
    elif args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    return parser, args


def mainloop(parser, args):
    """Implementation of this command."""
    print(repr(args))


def run():
    """Execute main loop."""
    try:
        setup()
        try:
            parser, args = make_argparser()
            mainloop(parser, args)
        except KeyboardInterrupt as exc:
            sys.stderr.flush()
            sys.exit(2)
        except IOError as exc:
            if exc.errno == errno.EPIPE:  # downstream is done with our output
                sys.stderr.flush()
                sys.exit(0)
            else:
                raise
    finally:
        logging.shutdown()


if __name__ == '__main__':
    run()
