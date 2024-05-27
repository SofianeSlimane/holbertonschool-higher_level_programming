#!/usr/bin/python3
""" This module contains the function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as myFile:
        json.dump(my_obj, myFile)
