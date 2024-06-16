#!/usr/bin/python3
"""This module contains the fetch_and_print_posts
and fetch_and_save_posts functions.
"""
import requests
import csv


def fetch_and_print_posts():
    """Sends a request to retrieve
    data from a website.

    The requests.get() returns a response object
    from the server.

    We can access the responses's status code,
    its text content and we can also use json()
    to parse the response into a JSON data object.

    Our function then prints every titles of all
    the posts by iterating through the json object
    (a list of dictionaries).
    """

    response_obj = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code:", response_obj.status_code)
    if response_obj.status_code == 200:
        json_obj = response_obj.json()
        for dictionary in json_obj:
            for key, values in dictionary.items():
                if key == "title":
                    print(values)


def fetch_and_save_posts():
    """Also sends a request to retrieve data
    from a websiter.
    The text content of the response is converted into
    a Python list of dictionaries of which are removed,
    the 'userId' keys.

    The list is then saved in a cvs file.
    It goes through different steps of formating:

        - The fieldnames (or columns), are defined
        in a list, and then written using writeheader().

        - The wirterows() method then takes each dictionary
        in our list and write them as rows'
    """
    my_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    my_json = my_response.json()
    if my_response.status_code == 200:
        my_list = []
        for dictionary in my_json:
            my_dict = {'id': dictionary.get('id'),
                       'title': dictionary.get('title'),
                       'body': dictionary.get('body')}
            my_list.append(my_dict)

        fieldnames = ["id", "title", "body"]

        with open("posts.csv", 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(my_list)
