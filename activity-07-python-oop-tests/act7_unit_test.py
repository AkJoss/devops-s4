# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 18:29:04 2025

@author: josea
"""

# Unit tests for the Racionales helper (coursework CI sample).
# @author José Alberto Rocha Munguía

import unittest
import act7_1_numeros


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")


class TestRacionales(unittest.TestCase):
    def test_print_hello(self):
        racionales = act7_1_numeros.Racionales(0)
        self.assertEqual(racionales.print_hello(), "Hello José")


if __name__ == "__main__":
    unittest.main()
