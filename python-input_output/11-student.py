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

    def to_json(self, attrs=None):
        """This function gives access to object representation.
        Args:
            attrs: list of string that contains the keys
            corresponding to the attriutes the user wants
            to retrieve.
        Returns: specific attributes asked by the user or
        every single attributes

        """
        dict_attributes = {}
        if type(attrs) is list:
            if all(type(str) for elements in attrs):
                for key in attrs:
                    for keys, values in self.__dict__.items():
                        if key == keys:
                            new_key = {keys: values}
                            dict_attributes.update(new_key)
                return dict_attributes

        else:
            return self.__dict__

    def reload_from_json(self, json):
        """This function replaces all the attributes
        of a Student object.
        Args:
            json: dictionary where key, is the name
            of the attribute and value, is the value
            to replace the current attribute's value
            with.

        Returns: The newly updated dictionary of attributes.
        """
        for key, value in json.items():
            for keys, values in self.__dict__.items():
                if key == keys:
                    self.__dict__[key] = value
        return self.__dict__
