#!/usr/bin/python3
""" This module contains the astract class Shape
and two subclasses of it: Circle and Rectangle.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Parent abstract class Shape """
    @abstractmethod
    def area(self):
        """ Intiates an area method for its subclasses. """
        ...

    @abstractmethod
    def perimeter(self):
        """ Intiates a perimeter method for its subclasses. """
        ...


class Circle(Shape):
    """ Circle subclasse of Shape """
    def __init__(self, radius):
        """ Implements Circle's constructor """
        self.radius = radius

    def area(self):
        """ Implements Circle's area method
        Returns: circle's area
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """ Implements Circle's perimeter method
        Returns: circle's perimeter
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """ Rectangle subclass of Shape """
    def __init__(self, width, height):
        """ Implements Rectangle's constructor
        Args:
            width: rectangle's width
            height: rectangle's height
        """
        self.width = width
        self.height = height

    def area(self):
        """ Implements Rectangle's area method
        Returns: rectaangle's area
        """
        return self.width * self.height

    def perimeter(self):
        """ Implements Rectangle's perimeter method
        Returns: rectangle's perimeter

        """
        return (self.width + self.height) * 2


def shape_info(form):
    """ Gives information about a shape object
    Args:
        form: shape object
    """
    print(f'Area: {form.area()}')
    print(f'Perimeter: {form.perimeter()}')


my_circle = Circle(3)
my_rectangle = Rectangle(4, 6)
shape_info(my_circle)
shape_info(my_rectangle)
