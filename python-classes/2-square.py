#!/usr/bin/python3
"""This module defines Square class."""


class Square:
    """Defines a square and its size."""
    def __init__(self, size=0):
        """Initializes a square using size.
        Args:
            size: Square size with default value of 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size value is negative
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
