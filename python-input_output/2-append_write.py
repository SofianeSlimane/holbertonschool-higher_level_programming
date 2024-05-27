#!/usr/bin/python3
""" This module contains the append_write function """


def append_write(filename="", text=""):
    """ This function appends content to a file
    given as a parameter.
    Args:
        filename: name of the file to append content in
        text: text to append to the file
    Returns: number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        num_char_a = myFile.write(text)
        return num_char_a
