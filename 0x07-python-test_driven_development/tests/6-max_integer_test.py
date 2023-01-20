#!/usr/bin/python3

"""Unittest for max_integer([]) function"""
import unittest

max = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max([]), None)
        self.assertAlmostEqual(max([8]), 8)
        self.assertAlmostEqual(max([1, 3, 4, 2]), 4)

    def test_inputs(self):
        self.assertRaises(ValueError, max, "boy")
