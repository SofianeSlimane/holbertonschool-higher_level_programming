#!/usr/bin/python3
"""This module contains the Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object
        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Method that prints the visual representation of a
        Rectangle object.
        """
        message = ""
        if self.__width == 0 or self.__height == 0:
            return message
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    message += "#"
                if i != self.__height - 1:
                    message += "\n"
        return message

    def __repr__(self):
        """Method that prints an informal string
        representation of the Rectangle object,
        in this case, the adress.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method called when an object is deleted"""
        print("Bye rectangle...")

    def area(self):
        """Computes the area of the Rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the Rectangle object"""
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2

        return perimeter

    @property
    def width(self):
        """Retrieves private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Changes width attribute value if necessary
        Args:
            value: Rectangle width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width value is negative
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Changes size attribute value if necessary
        Args:
            value: Rectangle height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height value is negative
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
