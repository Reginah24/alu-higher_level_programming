#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base
import json
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id_auto_assignment(self):
        """Test that id is correctly assigned when not provided"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
        b2 = Base()
        self.assertEqual(b2.id, 2)
        
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_manual_assignment(self):
        """Test that id is correctly assigned when provided"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None input"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_normal(self):
        """Test to_json_string with normal input"""
        input_list = [{"id": 12}]
        expected = json.dumps(input_list)
        self.assertEqual(Base.to_json_string(input_list), expected)
        self.assertIsInstance(Base.to_json_string(input_list), str)

    def test_from_json_string_none(self):
        """Test from_json_string with None input"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_normal(self):
        """Test from_json_string with normal input"""
        json_input = '[{"id": 89}, {"id": 12}]'
        expected = [{"id": 89}, {"id": 12}]
        self.assertEqual(Base.from_json_string(json_input), expected)


if __name__ == "__main__":
    unittest.main()
