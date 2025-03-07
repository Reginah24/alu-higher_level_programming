#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A base class for geometry objects"""

    def area(self):
        """Method that calculates area

        Raises:
            Exception: This method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates if value is a positive integer

        Args:
            name (str): name of the value
            value: the value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
