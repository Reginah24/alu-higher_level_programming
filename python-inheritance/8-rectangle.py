#!/usr/bin/python3
"""Define a Rectangle class that inherits from BaseGeometry."""
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
