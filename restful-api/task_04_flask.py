#!/usr/bin/python3
"""This module sets up a simple Flask Application"""
from flask import Flask, jsonify, request
app = Flask(__name__)

username_list = []
users = {}


@app.route("/")
def home():
    """Called when accessing home page"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Called when accessing /data URL"""
    return jsonify(username_list)


@app.route("/status")
def status():
    """Called when accessing /status URL"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Called when accessing /users/<username>.
    Args:
        username: retrieves the dynamic variable
        <username> and use it as a parameter.
    """
    users_data = users.get(username)
    if users_data is None:
        return {"error": "User not found"}
    else:

        return users_data


@app.route("/add_user", methods=['POST'])
def add_user():
    """Called when accessing /add_user. Only
    accepts POST requests.
    """
    data = request.get_json()
    users.update({1: "test"})

    message = {"message": "User added",
               "user": data}

    return message


if __name__ == "__main__":
    app.debug = True
    app.run()
