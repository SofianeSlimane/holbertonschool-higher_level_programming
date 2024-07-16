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
    if src == 'json':
        with open('products.json', 'r') as myFile:
            json_data = json.load(myFile)
        if _id is not None:
            for dictionary in json_data:
                if dictionary.get('id') == _id:
                    my_dict = dictionary
                    del my_dict['id']
                    return render_template('product_display.html', my_dict=my_dict)
        else:
            for product in json_data:
                del product['id']
            return render_template('product_display.html', my_dict=json_data)
    
    elif src == 'csv':
        with open('products.csv', 'r') as myFile:
            csvReader = csv.DictReader(myFile)
        if _id is not None:
            for row in csvReader:
                if row.get('id') == _id:
                    my_row = row
                    del my_row['id']
                    return render_template('product_display.html', my_dict=my_row)
        else:
            for row in csvReader:
                del row['id']
        return render_template('product_display.html', my_dict=csvReader)
    
    else:
        return render_template('product_display.html', error_message="Wrong source")

    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
