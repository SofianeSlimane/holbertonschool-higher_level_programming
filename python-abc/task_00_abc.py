#!/usr/bin/python3
""" This module contains the abstract class Animal,
and its subclasses: Dog and cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Abstract class which serves as
    a blueprint for our subclasses.
    """
    @abstractmethod
    def sound(self):
        """Sound method that must be created whithin any
        child classes othe Animale class.
        """
        pass


class Dog(Animal):
    """ Dog subclass """
    def sound(self):
        """ Returns dog sound """
        return "Bark"


class Cat(Animal):
    """ Cat subclass """
    def sound(self):
        """ Returns cat sound """
        return "Meow"
