#!/usr/bin/python3
""" This module contains the BaseGeometry class """


class BaseGeometry:
    """ This is the BaseGeometry class """
    def area(self):
        """ This is the area method which
        only raises an exception for now
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This method validates value.
        Args:
            name: name associated with the value.
            value: value
        Raise:
            TypeError: if value is not an integer.
            ValueError: if value is inferior or equal
            to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
