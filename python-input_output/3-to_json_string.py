#!/usr/bin/python3
""" This module contains the function to_json_string """
import json


def to_json_string(my_obj):
    """ This function returns the JSON representation
    (string representation) of an object.
    Args:
        my_obj: object to be converted into string representation
    """
    return json.dumps(my_obj)
