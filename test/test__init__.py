#! /usr/bin/env python
# .. coding: utf-8
# $Id$
# Author: Günter Milde <milde@users.sourceforge.net>
# Copyright: This module has been placed in the public domain.

"""
Test module for the docutils' __init__.py.
"""

import unittest
import sys
import DocutilsTestSupport              # must be imported before docutils
import docutils

class ApplicationErrorTests(unittest.TestCase):

    def test_message(self):
        err = docutils.ApplicationError('the message')
        self.assertEqual(str(err), 'the message')

    def test_non_ASCII_message(self):
        err = docutils.ApplicationError('\u0169')
        self.assertEqual(str(err), '\u0169')


if __name__ == '__main__':
    unittest.main()
