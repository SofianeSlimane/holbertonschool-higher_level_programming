#!/usr/bin/env python3
"""This module contains the CustomObject class"""
import pickle


class CustomObject:
    """Custom Object Class."""
    def __init__(self, name, age, is_student):
        """Constructor method.
        Args:
            name: name
            age (int): age
            is_student (bool): determines if object is student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Converts an object into a binary
        stream and writes it in a file.
        Args:
            filename: file binary stream will be
            written to.
        Returns: None if object cannot be serialized
        or, if the file is not found.
        """
        try:
            with open(filename, "wb") as myFile:
                pickle.dump(self, myFile)
        except pickle.PicklingError:
            return None
        except FileNotFoundError:
            return None

    def display(self):
        """Prints a formated object's
        attribute dictionary.
        """
        for key, value in self.__dict__.items():
            print("{}: {}".format(key, value))

    @classmethod
    def deserialize(cls, filename):
        """Converts a binary stream back into a
        Python object.
        Returns: None if object cannot be serialized
        or, if the file is not found.
        """
        try:
            with open(filename, "rb") as myFile:
                my_object = pickle.load(myFile)
                return my_object
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            return None
        except AttributeError:
            return None
        except EOFError:
            return None
        except ImportError:
            return None
        except IndexError:
            return None
