#!/usr/bin/python3
"""This module contains the fetch_and_print_posts
and fetch_and_save_posts functions.
"""
import requests
import csv


# Random print statements can be found in this code.
# These were used for testing purposes, don't mind
# them.
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

        # print("My json obj", json_obj)
    # print("My Response headers:", my_obj.headers)


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

    if my_response.status_code == 200:
        my_list = eval(my_response.text)
        # print(type(my_list))
        # print(my_list[0])
        # for dictionary in my_list:
        #    del dictionary['userId']
        # print(my_list)
        fieldnames = ["userId", "id", "title", "body"]

        with open("posts.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(my_list)

        # print(list(my_response.text))
