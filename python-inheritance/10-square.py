#!/usr/bin/python3
""" This module contains the Square class, a subclass of Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square, a subclass of Rectangle.
    """
    def __init__(self, size):
        """ Constructor method that
        initializes Square object attributes
        Args:
            size: square size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Computes square area"""
        return self.__size ** 2
