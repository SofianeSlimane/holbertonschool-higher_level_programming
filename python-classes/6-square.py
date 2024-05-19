#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Defines a square
    Attributes:
        size: represents a square size

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square object.
        Args:
            size: square size with default value of zero
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Computes the area of the square object
        Returns:
            int: area value
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the Square object with # signs"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    if not(self.__position[1] > 0):
                        print(" ", end="")
                    else:
                        print(" ", end="")
                        break
                for k in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Retrieves private instance attribute size"""
        return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Changes size attribute value if necessary
        Args:
            value: square size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size value is negative
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
