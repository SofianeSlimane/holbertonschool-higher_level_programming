#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Collection of test methods (test suite)"""

    def test_isempty(self):
        """Test with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_int(self):
        """Test list of postive integers"""
        self.assertEqual(max_integer([100, 50, 0]), 100)

    def test_max_negative_int(self):
        """Test list of negative integers"""
        self.assertEqual(max_integer([-1, -10, -100]), -1)

    def test_max_neg_pos_int(self):
        """Test list with mixed negative and positive integers"""
        self.assertEqual(max_integer([50, -1, -15]), 50)

    def test_max_string(self):
        """Test list of strings"""
        self.assertEqual(
                max_integer(["The", "One", "Piece", "is", "real"]), "real")

    def test_max_bool(self):
        """Test boolean"""
        self.assertEqual(max_integer([True, False]), True)
