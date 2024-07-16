#!/usr/bin/python3
"""This module contains a simple flask application"""
from flask import Flask, render_template
import json

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
