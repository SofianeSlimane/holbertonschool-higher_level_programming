#!/usr/bin/python3
""" This module contains the astract class Shape
and two subclasses of it: Circle and Rectangle.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """ Parent abstract class Shape """
    @abstractmethod
    def area(self):
        """ Intiates an area method for its subclasses. """
        pass

    @abstractmethod
    def perimeter(self):
        """ Intiates a perimeter method for its subclasses. """
        pass


class Circle(Shape):
    """ Circle subclasse of Shape """
    def __init__(self, radius):
        """ Implements Circle's constructor """
        self.radius = radius

    def area(self):
        """ Implements Circle's area method
        Returns: circle's area
        """
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        """ Implements Circle's perimeter method
        Returns: circle's perimeter
        """
        return 2 * 3.141592653589793 * self.radius


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


def shape_info(Shape):
    """ Gives information about a shape object
    Args:
        form: shape object
    """
    print(f'Area: {Shape.area()}')
    print(f'Perimeter: {Shape.perimeter()}')


circle = Circle(3)
rectangle = Rectangle(4, 6)
shape_info(circle)
shape_info(rectangle)
