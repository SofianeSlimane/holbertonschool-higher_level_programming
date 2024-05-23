#!/usr/bin/python3
"""This module contains the MyList class"""


class MyList(list):
    """ MyList inherits from the list class (and list method
    as well
    """
    def print_sorted(self):
        print(sorted(self))
