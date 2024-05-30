#!/usr/bin/python3
"""This module contains the serialize_and_save_to_file
and the load_and_deserialize.
"""
import json


def serialize_and_save_to_file(data, filename):
    """This function converts data into JSON
    format and save it in a file.
    Args:
        data: data to be converted and saved
        filename: file to save data into
    """
    with open(filename, 'w') as myFile:
        json.dump(data, myFile)


def load_and_deserialize(filename):
    """This function retrieves JSON data
    from a file, converts (deserialize) it
    to a Python dictionary object.
    Args:
        filename: file to retrieve JSON data from
    Returns: Python dictionary with the deserialized
    data.
    """
    with open(filename, 'r') as myFile:
        python_object = json.load(myFile)
        return python_object
