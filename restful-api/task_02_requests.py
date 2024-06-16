#!/usr/bin/python3
"""Testing checker"""
import requests
import csv


def fetch_and_print_posts():
    """Testing checker"""
    response_obj = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code: {}".format(response_obj.status_code))
    if response_obj.status_code == 200:
        json_obj = response_obj.json()
        for dictionary in json_obj:
            print(dictionary['title'])


def fetch_and_save_posts():
    """Testing checker"""
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
