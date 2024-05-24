#!/usr/bin/python3
""" This module contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """ Checks if an object is an instance of a class
    or, if an object is an instance of a subclass of
    the class specified.
    Args:
        obj: instance
        a_class: class the instance will compared to
    Returns:
        True: if obj is an instance of a_class or if
        obj is an instance of a subclass of a_class
        False: Otherwise
    example:
        a = 1
        is_kind_of_class(a, object)
        --> True
        Here our function checks if a is an instance
        of object, it's not.
        It then checks if a, is an instance of a class,
        that is a subclass of object.
        a is of class int, int is a subclass of object,
        so it returns True.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
