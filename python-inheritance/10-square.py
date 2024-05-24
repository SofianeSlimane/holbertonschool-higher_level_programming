#!/usr/bin/python3
""" This module contains the Square class, a subclass of Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ Square, a subclass of Rectangle which
        inherits from its attributes and also
        integer_validator.
        Args:
            size: square size
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Computes square area"""
        return self.__size ** 2
