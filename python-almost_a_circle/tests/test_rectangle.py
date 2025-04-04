ts/test_rectangle.py
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_id(self):
        r1 = Rectangle(2, 3, id=100)
        self.assertEqual(r1.id, 100)

if __name__ == "__main__":
    unittest.main()
