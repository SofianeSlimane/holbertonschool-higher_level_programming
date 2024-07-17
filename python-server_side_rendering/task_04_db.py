#!/usr/bin/python3
"""This module contains a simple flask application"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def create_database():
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    price REAL NOT NULL
                )
            ''')
            cursor.execute('''
                INSERT INTO Products (id, name, category, price)
                VALUES
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99)
            ''')
            conn.commit()
            conn.close()
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
    elif src == 'sql':
        my_lista = []
        con = sqlite3.connect('products.db')
        cur = con.cursor()
        res = cur.execute("SELECT * FROM Products")
        table = cur.fetchall()
        for tup in table:
                my_diplo = dict(id = tup[0], name = tup[1], category = tup[2], price = tup[3])
                my_lista.append(my_diplo)
            
        if _id is not None:
            for hawk in my_lista:
                    if str(hawk.get('id')) != _id:
                        id_exists = False
                    else:
                        id_exists = True
                        break
            if id_exists == False:
                return render_template('product_display.html', product_not_found='Product not found')
            for owl in my_lista:
                if str(owl.get('id')) != _id:
                    my_lista.remove(owl)
            for parrot in my_lista:
                parrot.pop('id')
            return render_template('product_display.html', my_dict=my_lista)



      
        else:
            
            for elem in my_lista:
                elem.pop('id')    
            return render_template('product_display.html', my_dict=my_lista)


    else:
        return render_template('product_display.html', error_message="Wrong source")

    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    create_database()
