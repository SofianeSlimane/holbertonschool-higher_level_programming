#!/usr/bin/python3
"""This module contains the Rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object
        Args:
            width: width
            height: height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Changes size attribute value if necessary
        Args:
            value: Rectangle width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width value is negative
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Changes size attribute value if necessary
        Args:
            value: Rectangle height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height value is negative
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
