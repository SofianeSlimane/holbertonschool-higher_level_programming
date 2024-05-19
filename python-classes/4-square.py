#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Defines a square
    Attributes:
        size: represents a square size

    """
    def __init__(self, size=0):
        """Initializes a Square object.
        Args:
            size: square size with default value of zero
        """
        self.__size = size

    def area(self):
        """Computes the area of the square object
        Returns:
            int: area value
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Changes size attribute value if necessary
        Args:
            value: square size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size value is negative
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
