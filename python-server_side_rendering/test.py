#!/usr/bin/python3
import json
import csv

#with open("items.json", 'r') as myfile:
    #my_obj = json.load(myfile)

#print(type(my_obj))
#print(my_obj)

#for key, value in my_obj.items():
    #for element in value:
        #print(element)

print("data from csv file")
print("----------------------------------")
with open("products.csv", 'r') as myFile:
    csvReader = csv.DictReader(myFile)
    for row in csvReader:
        print(type(row))
        print(row)

print("data from json file")
print("----------------------------------")
with open("products.json", 'r') as myfile:
    my_obj = json.load(myfile)
    print(type(my_obj))
    for products in my_obj:
        print(products)
    
print("accessible", my_obj)
print("Acessible too", csvReader)