# tests/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0  # Reset between tests

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_mixed_ids(self):
        b1 = Base()
        b2 = Base(55)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 55)
        self.assertEqual(b3.id, 2)

if __name__ == "__main__":
    unittest.main()
