#!/usr/bin/python3
"""
Unittest for max_integer([])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test for different use case of the function max_integer
    """

    def test_max_int_basic(self):
        """Test basic usage
        """
        self.assertEqual(max_integer([1, 5, 2, 12, 10, 3], 12))

    def test_max_int_empty(self):
        """Text empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_max_int_negative(self):
        """Test with negative int
        """
        self.assertEqual(max_integer([-1, -2, -18], -1))

    def test_max_int_negative_positive:
        """Test with negative and positive int
        """
        self.assertEqual(max_integer([0, -1, 5, -18, 3], 5))

    def test_max_int_one(self):
        """
        Test with one element in the list
        """
        self.assertEqual(max_integer([2], 2))

if __name__ == "__main__":
    unittest.main()
