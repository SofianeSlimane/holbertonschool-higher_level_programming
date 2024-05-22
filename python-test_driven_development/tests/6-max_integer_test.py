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
    def test_max_negative_int(self):
        self.assertEqual(max_integer([-1, -10, -100]), -1)
    def test_max_neg_pos_int(self):
        self.assertEqual(max_integer([50, -1, -15]), 50)
    def test_max_string(self):
        self.assertEqual(max_integer(["The", "One", "Piece", "is", "real"]), "real")
    def test_max_bool(self):
        self.assertEqual(max_integer([True, False]), True)
