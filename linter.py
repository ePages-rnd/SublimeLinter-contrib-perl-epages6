#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jonas Gratz
# Copyright (c) 2015 Jonas Gratz
#
# License: MIT
#

"""This module exports the PerlEpages6 plugin class."""

import sublime
from SublimeLinter.lint import Linter, util

class PerlEpages6(Linter):

    """Provides an interface to perl on an epages6 virtual machine from a local machine.
    Requires a configured copy of the Epages6 plugin (see https://github.com/ePages-rnd/sublimetext-epages6)."""

    def cmd(self):
        return [self.executable_path, sublime.load_settings('Epages6.sublime-settings').get('path'), '--vm=' + self.view.settings().get('ep6_vm'), '--lint', '@'];

    executable = 'perl'
    syntax = ('modernperl', 'perl')
    regex = r'(?P<message>.+?) at .+? line (?P<line>\d+)(, near "(?P<near>.+?)")?'
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'pm'
