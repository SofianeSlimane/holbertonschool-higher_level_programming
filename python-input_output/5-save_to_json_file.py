#!/usr/bin/python3
"""This module contains the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """This function saves an object in a text file in its JSON representation.
    Args:
        my_obj: object to be saved in file
        filename: file
    """
    with open(filename, 'w') as myFile:
        json.dump(my_obj, myFile)
