#!/usr/bin/python3
"""Define a Rectangle class that inherits from BaseGeometry."""
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
