#!/usr/bin/python3
"""This module contains the class_to_json function"""


def class_to_json(obj):
    """This function returns the attributes
    of a given object. It uses the __dict__
    proprety to do so. __dict__ is a dictionary
    that stores the attributes of an object.

    Args:
        obj: class object

    Returns: __dict__, an dictionary of the object's attributes

    """
    return obj.__dict__
