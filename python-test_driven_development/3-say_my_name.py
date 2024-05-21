#!/usr/bin/python3
"""This module ocntains the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """ This function prints a first and last name
    Args:
        first_name = first name
        last_name = last name
    Raises:
        TypeError: if one of parameter is not a string
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
