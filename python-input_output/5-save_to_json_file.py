#!/usr/bin/python3
""" This module contains the function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ This function writes an object to a text file.
    The dump function first serializes the Python object into
    JSON representation, and then saves it in the given file name.
    Args:
        my_obj: object to be written into file
        filename: file to write object into
    """
    with open(filename, 'w') as myFile:
        json.dump(my_obj, myFile)
