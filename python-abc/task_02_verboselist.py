#!/usr/bin/python3
""" This module contains the VerboseList,
a class derived from list.
"""


class VerboseList(list):
    """ VerboseList class """
    def append(self, item):
        """ Customed append method """
        super().append(item)
        print(f'Added [{item}] to the list.')

    def extend(self, item):
        """ Customed extend method """
        x = len(item)
        super().extend(item)
        print(f'Extended the list with [{x}] items.')

    def remove(self, item):
        """ Customed remove method """
        print(f'Removed [{item}] from the list.')
        super().remove(item)

    def pop(self, index=-1):
        """ Customed pop method """
        item = self[index]
        print(f'Popped [{item}] from the list.')
        super().pop(index)
