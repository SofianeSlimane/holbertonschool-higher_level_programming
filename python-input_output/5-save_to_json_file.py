#!/usr/bin/python3
""" This module contains the function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """This function saves an object in a text file in its JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
