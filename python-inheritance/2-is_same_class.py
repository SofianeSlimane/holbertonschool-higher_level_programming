#!/usr/bin/python3
""" This module contains the is_same_class function """


def is_same_class(obj, a_class):
    """ Checks if an object is an instance of a class.
    Args:
        obj: instance
        a_class: class the instance will compared to
    Returns:
        True: if obj is an instance of a_class
        False: Otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
