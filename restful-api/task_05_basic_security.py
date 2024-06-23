#!/usr/bin/python3
"""This module contains Flask application that
protects certain routes either with basic authentification
or with a JSON web token."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "my secret"
jwt = JWTManager(app)

users = {
      "user1": {
                "username": "user1",
                "password": generate_password_hash("hello"),
                "role": "user"
                },
      "admin1": {
                "username": "admin1",
                "password": generate_password_hash("bye"),
                "role": "admin"
                }
  }


@auth.verify_password
def verify_password(username, password):
    """Checks if given creditentials are the same in users dictionary"""
    if username in users and \
            check_password_hash(users.get(username)['password'], password):
        return username


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic():
    """Route needs basic auth to be accessed."""
    return jsonify("Basic Auth: Access Granted")


@app.route("/login", methods=['POST'])
def jwt_ath():
    """Logs a user if it exists, returns a JWT to the user
    so he can auth with it."""
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and check_password_hash(
            users.get(username)["password"], password):

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify("Incorrect username or password"), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def protected():
    """JWT protected route, can oly be accessed if
    user logged in previously and was given a JWT."""
    current_user = get_jwt_identity()
    return jsonify("JWT Auth: Access Granted")


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    """Only allows admin with a valid JWT to access the route"""
    user_identity = get_jwt_identity()
    if user_identity in users and users.get(user_identity)['role'] == "admin":
        return jsonify("Admin Access: Granted")
    else:
        return jsonify("Forbidden"), 401

# Custom error handlers


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """JWT missing or invalid."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Token is invalid."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Expired JWT"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Revoked JWT """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Fresh token required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
