#!/bin/python3
from flask import Flask, jsonify, request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'myKey.20202030'
jwt = JWTManager(app)

USER_DB = {
    "test": "password"
}

@app.route('/')
def hello():
    return 'hello'


@app.route('/rest/login', methods=['POST'])
def login():
    data = request.get_json()

    username, password = None, None
    if 'username' in data.keys():
        username = data['username']
    if 'password' in data.keys():
        password = data['password']

    if username and password:
        if username not in USER_DB.keys():
            return jsonify({"ERR": "UNAUTHORIZED"}), 401

        if password != USER_DB[username]:
            return jsonify({"ERR": "INVALID_PASSWORD"}), 401

        access_token = create_access_token(username)
        return jsonify(access_token=access_token, username=username), 200
    else:
        return jsonify({"ERR": "BAD_REQUEST"}), 400


@app.route("/rest/cities", methods=['POST'])
@jwt_required()
def cities():
    """
    """
    return jsonify({"BLA": "BLA"}), 200
