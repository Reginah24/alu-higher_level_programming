# main.py
from models.rectangle import Rectangle
from models.square import Square

# Create a rectangle
r = Rectangle(4, 6, 2, 3, 42)
print(f"Rectangle Area: {r.area()}")  # Should print 24

# Create a square
s = Square(5, 1, 1, 99)
print(s)  # Should print: [Square] (99) 1/1 - 5
