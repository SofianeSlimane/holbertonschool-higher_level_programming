#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Defines a square.

    Attributes:
        size: integer represent square size
    """
    def __init__(self, size=0):
        """Initializes square object.
        Args:
            size: square size

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

    def area(self):
        """Computes area.
        Returns: area

        """
        return self.__size ** 2
