#!/usr/bin/python3
"""This module contains the Student class"""


class Student:
    """This class defines a student with few attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function gives access to object representation.
        Returns: object's __dict__
        """
        return self.__dict__
