#!/usr/bin/python3
"This module defines add_integer which returns the sum of two integers."


def add_integer(a, b=98):
    """This function computes the sum of two integers.
    Args:
        a: 1st value should be an integer or
        be converted into one if its a float.

        b: 2nd value should be an integer or
        be converted into one if it's a float.

    Raises:
        TypeError: if a or b is not an integer.

    Returns:
        The sum of both integers.

    """
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    elif isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, int) is False:
        raise TypeError("b must be an integer")
    return a + b
