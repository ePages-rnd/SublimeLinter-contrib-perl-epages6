#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jonas Gratz
# Copyright (c) 2014 Jonas Gratz
#
# License: MIT
#

"""This module exports the PerlEpages6 plugin class."""

from SublimeLinter.lint import Linter, util


class PerlEpages6(Linter):

    """Provides an interface to perl on an epages6 virtual machine from a local OS X.
    Requires a configured copy of the Flakes plugin (see https://github.com/ePages-rnd/sublimetext-epages-flakes)."""

    syntax = ('modernperl', 'perl')
    cmd = 'perlc @'
    regex = r'(?P<message>.+?) at .+? line (?P<line>\d+)(, near "(?P<near>.+?)")?'
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'pm'
