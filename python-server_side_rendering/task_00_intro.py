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
    index = 1
    file_path = "output_X.txt"
    new_str = template
    if type(template) is not str:
        raise TypeError(f"{type(template)} is invalid")
    elif type(attendees) is not list:
        raise TypeError(f"{type(attendees)} is invalid")
    for items in attendees:
        if type(items) is not dict:
            raise TypeError("attendees must be a list of dictionnaries")
    if len(template) == 0:
        raise ValueError("Template is empty, no output files generated")
    elif len(attendees) == 0:
        raise ValueError("No data provided, no output files generated.")

    for people in attendees:
        for key, value in people.items():
            if value is None:
                new_str = new_str.replace('{{{}}}'.format(key), "N/A")

            else:
                try:
                    new_str = new_str.replace('{{{}}}'.format(key), value)
                except ValueError:
                    raise ValueError
    print(new_str)
    for people in attendees:
        if os.path.exists("output_{}.txt".format(index)):
            pass
            with open('output_{}.txt'.format(index), 'w') as file:
                file.write(new_str)
                index += 1
