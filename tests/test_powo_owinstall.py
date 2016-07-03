#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_powo_owinstall
----------------------------------

Tests for `powo_owinstall` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from powo_owinstall import powo_owinstall
from powo_owinstall import cli



class TestPowo_owinstall(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'powo_owinstall.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())
