#!/usr/bin/python3
""" This module contains the read_file function """


def read_file(filename=""):
    """ This function reads the content of a file
    given as a parameter.
    Args:
        filename: name of the file to read from
    """
    with open(filename, 'r', encoding="utf-8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")
