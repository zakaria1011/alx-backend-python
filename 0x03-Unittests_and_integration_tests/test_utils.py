#!/usr/bin/python3
""" unittest"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ testing the function access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nasted_map, path, expected):
        """ testing nested map with various input"""
        self.assertEqual(access_nested_map(nasted_map, path), expected)


if __name__ == '__main__':
    unittest.main
