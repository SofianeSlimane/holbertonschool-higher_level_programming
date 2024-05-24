#!/usr/bin/python3
""" This module contains the BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Computes and returns the area
        of a Rectangle object """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a user-friendly representation
        of a square object.
        """
        return f'[Rectangle] {self.__width}/{self.__height}'
