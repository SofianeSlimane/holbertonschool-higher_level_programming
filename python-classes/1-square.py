#!/usr/bin/python3
"This module contains the Square class"


class Square:
    """Defines a square and its size.
    Attributes:
        size: integer that represents square size.
    """
    def __init__(self, size):
        """Initializes a square using size.

        Args:
         size: Defines the size of the square
         """
        self.__size = size
