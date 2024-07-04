# Import necessary modules and functions
import re
import bcrypt
import jwt
import datetime
import time
import os
from dotenv import load_dotenv
from pymongo.errors import PyMongoError
from html import escape
from flask import current_app, request, jsonify, make_response
from flask_jwt_extended import create_access_token

# Load environment variables
load_dotenv()
secret_key = os.getenv("SECRET_KEY")

# Function to create a user
def create_user():
    try:
        db = current_app.config["db"]
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        confirm_password = request.json.get("confirmPassword")
        # Trim whitespace and sanitize input
        username = escape(username.strip())
        email = escape(email.strip())
        password = escape(password.strip())
        confirm_password = escape(confirm_password.strip())
        # Data validation
        if username == "" or email == "" or password == "":
            return make_response(jsonify(error="All fields are required"), 400)
        if password != confirm_password:
            return make_response(jsonify(error="Passwords do not match"), 400)
        if db.Users.count_documents({"email": email}) > 0:
            return make_response(jsonify(error="Email already in use"), 400)
        if db.Users.count_documents({"username": username}) > 0:
            return make_response(jsonify(error="Username already in use"), 400)
        if len(password) < 8:
            return make_response(jsonify(error="Password must be at least 8 characters"), 400)
        # Email validation
        match = re.match(r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$", email)
        if match is None:
            return make_response(jsonify(error="Invalid email"), 400)
        # Hash password
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        # Insert user into MongoDB
        result = db.Users.insert_one({"username": username, "email": email, "password": password_hash})
        return make_response(jsonify(message="User created successfully"), 200)
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)

# Function to login a user
def login_user():
    try:
        db = current_app.config["db"]
        db_users = db["Users"]
        username = request.json.get("username")
        password = request.json.get("password")
        username = username.strip()
        password = password.strip()
        # Data validation
        user = db_users.find_one({"username": username})
        if user is None:
            return make_response(jsonify(error="Username not found"), 404)
        else:
            stored_password = user["password"]
            password = password.encode("utf-8")
            if bcrypt.checkpw(password, stored_password):
                # Create JWT for user
                expires = datetime.timedelta(minutes=30)
                token = create_access_token(identity=str(user["_id"]), expires_delta=expires)
                return make_response(jsonify(success="Logged In successfully", token=token), 200)
            else:
                return make_response(jsonify(error="Invalid Password"), 403)
    except Exception as e:
        return make_response(jsonify(error=str(e)), 500)

# Function to register user routes
def register_user_routes(app):
    app.add_url_rule('/createUser', view_func=create_user, methods=['POST'])
    app.add_url_rule('/login', view_func=login_user, methods=['POST'])