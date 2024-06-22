#!/usr/bin/python3
"""This module sets up a simple Flask Application"""
from flask import Flask, jsonify, request
app = Flask(__name__)


users = {}


@app.route("/")
def home():
    """Called when accessing home page"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Called when accessing /data URL"""
    return jsonify(list(users.keys()))


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
    user_data = users.get(username)
    if user_data is None:
        return {"error": "User not found"}
    return jsonify(user_data)


@app.route("/add_user", methods=['POST'])
def add_user():
    """Called when accessing /add_user. Only
    accepts POST requests.
    """
    my_json_dict = request.get_json()
    username = my_json_dict.get("username")
    if username is None:
        return {"error": "User not found"}
    # print(data)
    # print(type(data))
    users[username] = my_json_dict
    # print(users)

    message = {"message": "User added",
               "user": my_json_dict}

    return jsonify(message)


if __name__ == "__main__":
    app.debug = True
    app.run()
