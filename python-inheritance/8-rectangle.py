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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ This is the Rectangle class
    which is a subclass of BaseGeometry.
    """
    def __init__(self, width, height):
        """ Construtor method that will initialize
        every Rectangle objects.
        Args:
            width: width
            height: height
        """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        self.__height = height
