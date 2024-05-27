#!/usr/bin/python3
"""This module contains the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """This functiion reads a JSON file and
    parse its contents into a Python Object.
    Args:
        filename: name of the file that contains JSON data

    Returns: Python object representing the JSON data
    """
    with open(filename, 'r') as myFile:
        python_object = json.load(myFile)
        return python_object
