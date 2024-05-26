#!/usr/bin/python3
""" This module contains the SwimMixin and FlyMixin and
a subclass Dragon that inherits from both.
"""


class SwimMixin:
    """ SwimMixin mixin """
    def swim(self):
        """ swim method """
        print("The creature swims!")


class FlyMixin:
    """ FlyMixin mixin """
    def fly(self):
        """ fly method """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ Dragon subclass that inherits from two
    mixins.
    """
    def roar(self):
        """ roar method unique to Dragon """
        print("The dragon roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
