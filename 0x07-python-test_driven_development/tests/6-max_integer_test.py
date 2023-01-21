#!/usr/bin/python3
"""Unittest for max_integer"""


import unittest
module = __import__("6-max_integer")
max_integer = module.max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer"""

    def test_module_docstring(self):
        self.assertTrue(len(module.__doc__) > 1)

    def test_function_docstring(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 3, 1, 4, 2]), 5)
        self.assertEqual(max_integer([0, 2, 1, 5, 7, 4]), 7)
        self.assertEqual(max_integer([-2, 0, -3, -5, -1]), 0)
        self.assertEqual(max_integer([-2, -4, -3, -5, -1]), -1)
        self.assertEqual(max_integer([-1, 1]), 1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
