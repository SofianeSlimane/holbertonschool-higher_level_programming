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
        for i in range(len(text)):
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print(text[i], end="")
                print()
                print()
            elif text[i] == " ":
                i += 1
            else:
                print(text[i], end="")
    else:
        raise TypeError("text must be a string")
