#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_isempty(self):
        self.assertEqual(max_integer([]), None)
    def test_max_int(self):
        self.assertEqual(max_integer([100, 50, 0]), 100)
