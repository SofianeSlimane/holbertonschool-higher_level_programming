#!/usr/bin/python3
"""This module contains the square class"""


class Square:
    """Defines a square and its size."""
    def __init__(self, size=0):
        """Initializes a square using size.
        Args:
            size: Square size with default value of 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
