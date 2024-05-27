#!/usr/bin/python3
""" This module containes the wrtie_file function """


def write_file(filename="", text=""):
    """ This function writes text in the file
    given as a parameter.
    Args:
        filename: name of the file to write to
        text: text to be written in file
    Returns: number of character written
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        num_char_w = myFile.write(text)
        return num_char_w
