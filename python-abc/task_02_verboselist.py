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
        len_list_before = len(self)
        super().extend(item)
        len_list_after = len(self)
        x = len_list_after - len_list_before
        print(f'Extended the list with [{x}] items.')

    def remove(self, item):
        """ Customed remove method """
        print(f'Removed [{item}] from the list.')
        super().remove(item)

    def pop(self, index=-1):
        """ Customed pop method """
        print(f'Popped [{self[index]}] from the list.')
        super().pop(index)


my_list = VerboseList([4, 6, 9])
my_list.append(2)
my_list.extend([4, 3, 9])
my_list.remove(3)
my_list.pop()
my_list.pop(4)
