#!/usr/bin/python3
""" This module contains the function from_json_string """
import json


def from_json_string(my_str):
    """ This function returns an object represented
    by a JSON string.
    Args:
        my_string: JSON representation to be converted into Python object

    Returns: object represented by JSON

    """
    return json.loads(my_str)
