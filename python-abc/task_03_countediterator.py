#!/usr/bin/python3
""" This module contains the CountedIterator class """


class CountedIterator:
    """ The CountedIterator class is a
    class that extends the built-in iterator obtained from
    the iter function.
    """
    def __init__(self, some_iterable, counter=0):
        """ Initializes object.
        Args:
            some_iterable: iterable to iterate over
            counter: number of items that we iterated over
        """
        self.iterator = iter(some_iterable)
        self.counter = counter

    def get_count(self):
        """ Returns the current value of the counter """
        return self.counter

    def __next__(self):
        """ Returns the next item in the iterable """
        self.counter += 1
        try:
            item = next(self.iterator)
            return item
        except StopIteration:
            raise StopIteration
