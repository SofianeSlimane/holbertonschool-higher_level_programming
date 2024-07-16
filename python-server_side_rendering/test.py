#!/usr/bin/python3
import json


with open("items.json", 'r') as myfile:
    my_obj = json.load(myfile)

#print(type(my_obj))
#print(my_obj)

for key, value in my_obj.items():
    for element in value:
        print(element)