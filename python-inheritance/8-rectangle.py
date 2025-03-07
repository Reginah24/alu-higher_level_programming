#!/usr/bin/python3
"""Module for Rectangle class inheriting from BaseGeometry."""

from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize a new Rectangle instance."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
