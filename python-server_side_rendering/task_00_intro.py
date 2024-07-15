#!/usr/bin/python3
"""This module contains the generate_invitations method"""
import os


def generate_invitations(template, attendees):
    """Generates a personalized invitation
        Args:
            template (str): invitation message with placeholders
            for personalized values.

            attendees (list): list of dictionary of attendees
            where each value replaces its respective value
            in template.
            """
    if type(template) is not str:
        print(f"{type(template)} is invalid")
        exit()
    elif type(attendees) is not list:
        print(f"{type(attendees)} is invalid")
        exit()
    elif len(template) == 0:
        print("Template is empty, no output files generated.")
        exit()
    elif len(attendees) == 0:
        print("No data provided, no output files generated.")
        exit()

    for items in attendees:
        if type(items) is not dict:
            print(f"{type(items)}")
            exit()

    index = 1

    for people in attendees:
        new_str = template
        for key, value in people.items():
            if value is None:
                new_str = new_str.replace('{{{}}}'.format(key), "N/A",
                                          1)
            else:
                try:
                    new_str = new_str.replace('{{{}}}'.format(key), value,
                                              1)
                except ValueError:
                    raise ValueError
        if not os.path.exists("output_{}.txt"):
            try:
                with open('output_{}.txt'.format(index), 'w') as file:
                    file.write(new_str)
            except FileNotFoundError:
                raise FileNotFoundError
            except ImportError:
                raise ImportError
            except EOFError:
                raise EOFError

        index += 1
