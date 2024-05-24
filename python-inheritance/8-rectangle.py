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
