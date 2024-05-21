#!/usr/bin/python3
"""This module contains the text_indentation function"""


def text_indentation(text):
    """This functions prints a string
    and 2 blank lines when it encounters
    certain characters in a string
    Args:
        string: string
    """
    if isinstance(text, str):
        s1 = text.replace(". ", ".\n")
        s1 = s1.replace("? ", "?\n")
        s1 = s1.replace(": ", ":\n")
        for i in range(len(s1)):
            if s1[i] == "." or s1[i] == "?" or s1[i] == ":":
                print(s1[i], end="")
                print()
            else:
                print(s1[i], end="")
    else:
        raise TypeError("text must be a string")
