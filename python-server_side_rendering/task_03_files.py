#!/usr/bin/python3
"""This module contains a simple flask application"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Contact page"""
    with open('items.json', 'r') as myFile:
        my_list = json.load(myFile)
    
    return render_template('items.html', my_list=my_list)

@app.route('/products')
def data():
    """Contact page"""
    src = request.args.get('source')
    _id = request.args.get('id')
    id_exists = True
    if src == 'json':
        with open('products.json', 'r') as myFile:
            json_data = json.load(myFile)
            if _id is not None:
                for trex in json_data:
                    if str(trex.get('id')) != _id:
                        id_exists = False
                    else:
                        id_exists = True
                        break
                        
                if id_exists == False:
                    return render_template('product_display.html', product_not_found='Product not found')
                for dictionary in json_data:
                
                    if str(dictionary.get('id')) != _id:
                        
                        json_data.remove(dictionary)
                for denver in json_data:
                    denver.pop('id')
                        
                return render_template('product_display.html', my_dict=json_data)
            else:
                for product in json_data:
                    del product['id']
                return render_template('product_display.html', my_dict=json_data)
        
    elif src == 'csv':
        with open('products.csv', 'r') as myFile:
            csvReader = csv.DictReader(myFile)
            my_list = []
            for row in csvReader:
                my_list.append(row)
            if _id is not None:
                for tyrano in my_list:
                    if str(tyrano.get('id')) != _id:
                        id_exists = False
                    else:
                        id_exists = True
                        break
                if id_exists == False:
                    return render_template('product_display.html', product_not_found='Product not found')
                for dico in my_list:
                    if str(dico.get('id')) != _id:
                        my_list.remove(dico)
                for dino in my_list:
                    dino.pop('id')
                return render_template('product_display.html', my_dict=my_list)
            else:
                for element in my_list:
                    element.pop('id')
                        
                return render_template('product_display.html', my_dict=my_list)
    
    else:
        return render_template('product_display.html', error_message="Wrong source")

    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
