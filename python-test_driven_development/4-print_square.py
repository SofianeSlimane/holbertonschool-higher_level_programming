#!/usr/bin/python3
"""This module contains the print_square function"""


def print_square(size):
    """This function prints a square
    Args:
        size: size of square
    Raises:
        TypeError: if size is not an integer, is less than 0 or is a float
        and less than 0
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print()
