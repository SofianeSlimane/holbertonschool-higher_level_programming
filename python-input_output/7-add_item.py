#!/usr/bin/python3
"""This module contains a script that adds all arguments
to a list and save them them to a file. The list is then
retrieved as a Python Object.
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = load_from_json_file("add_item.json")
my_list = sys.argv
my_list.pop(0)
save_to_json_file(my_list, "add_item.json")
