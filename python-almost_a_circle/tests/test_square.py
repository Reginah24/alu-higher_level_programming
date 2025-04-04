# tests/test_square.py
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_square_size(self):
        s = Square(5)
        self.assertEqual(s.width, 5)

    def test_str(self):
        s = Square(3, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 3")

if __name__ == "__main__":
    unittest.main()
