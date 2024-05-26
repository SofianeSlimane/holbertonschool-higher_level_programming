#!/usr/bin/python3
""" This module contains the Fish and Bird Parents classes
and a FlyingFish class which inherits from both """


class Fish:
    """ Parent Fish class. """
    def swim(self):
        """ Fish swim method. """
        print("The fish is swimming")

    def habitat(self):
        """ Fish habitat method. """
        print("The fish lives in water")


class Bird:
    """ Parent Bird class. """
    def fly(self):
        """ Bird fly method """
        print("The bird is flying")

    def habitat(self):
        """ Bird habitat method. """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """ FlyingFish fly method which overides Bird
        fly method thanks to MRO.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """ FlyingFish swim method which overides Fish
        swim method thanks to MRO.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


print(FlyingFish.mro())
