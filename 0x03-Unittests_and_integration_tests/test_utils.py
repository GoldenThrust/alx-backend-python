#!/usr/bin/env python3
""" Utility Test Case """
from typing import Mapping, Sequence, Dict, Callable

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Blueprint to Tests access nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: int
    ) -> None:
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ) -> None:
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Blueprints to test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url: str, payload: Dict) -> None:
        """Test get_json method"""
        values = {"json.return_value": payload}
        with patch("requests.get", return_value=Mock(**values)) as mock:
            self.assertEqual(get_json(url), payload)
            mock.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Blueprint to test memoization"""

    def test_memoize(self) -> None:
        """Method to test memoization"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            Test = TestClass()
            Test.a_property()
            Test.a_property()
            mock.assert_called_once()
