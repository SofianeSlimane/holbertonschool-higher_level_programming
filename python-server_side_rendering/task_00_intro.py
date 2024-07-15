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

    for items in attendees:
        if type(items) is not dict:
            raise TypeError(f"{type(items)} is invalid")

    index = 1

    for people in attendees:
        new_str = template
        for key, value in people.items():
            if value is None or value is "":
                new_str = new_str.replace('{{{}}}'.format(key), f"{key}:N/A",
                                          1)
            else:
                try:
                    new_str = new_str.replace('{{{}}}'.format(key), value,
                                              1)
                except ValueError:
                    raise ValueError

        with open('output_{}.txt'.format(index), 'w') as file:
            file.write(new_str)

        index += 1
