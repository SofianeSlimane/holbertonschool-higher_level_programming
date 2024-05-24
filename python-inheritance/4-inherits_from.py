#!/usr/bin/python3
""" This module contains the inherits_from function """


def inherits_from(obj, a_class):
    """ Checks if an object is an instance of a class.
    Args:
        obj: instance
        a_class: class the instance will compared to
    Returns:
        True: If obj is an instance of a class that inherited
        directly or inderictly from another class.
        False: Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
