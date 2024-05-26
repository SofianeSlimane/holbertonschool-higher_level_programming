#!/usr/bin/python3
""" This module contains the VerboseList,
a class derived from list.
"""


class VerboseList(list):
    """ VerboseList class """
    def append(self, item):
        """ Customed append method """
        try:
            super().append(item)
            print(f'Added [{item}] to the list.')
        except TypeError:
            raise TypeError

    def extend(self, item):
        """ Customed extend method """
        try:
            x = len(item)
            super().extend(item)
            print(f'Extended the list with [{x}] items.')
        except TypeError:
            raise TypeError

    def remove(self, item):
        """ Customed remove method """
        try:
            print(f'Removed [{item}] from the list.')
            super().remove(item)
        except ValueError:
            raise ValueError

    def pop(self, index=-1):
        """ Customed pop method """
        try:
            item = self[index]
            print(f'Popped [{item}] from the list.')
            super().pop(index)
        except IndexError:
            raise IndexError
