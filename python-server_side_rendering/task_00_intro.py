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
        raise TypeError(f"{type(template)} is invalid")

    elif type(attendees) is not list:
        raise TypeError(f"{type(attendees)} is invalid")

    elif len(template) == 0:
        raise ValueError("Template is empty, no output files generated.")

    elif len(attendees) == 0:
        raise ValueError("No data provided, no output files generated.")

    for items in attendees:
        if type(items) is not dict:
            raise TypeError(f"{type(items)} is invalid")

    index = 1

    for people in attendees:
        new_str = template
        for key, value in people.items():
            if value is None:
                new_str = new_str.replace('{{{}}}'.format(key), f"{key}:N/A")
            else:
                try:
                    new_str = new_str.replace('{{{}}}'.format(key), value)
                except ValueError:
                    raise ValueError
        if not os.path.exists("output_{}.txt".format(index)):
            with open('output_{}.txt'.format(index), 'w') as file:
                file.write(new_str)
        index += 1
