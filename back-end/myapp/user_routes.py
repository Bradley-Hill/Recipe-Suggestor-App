# User and login/auth routes to be kept here
import re
import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv
from pymongo.errors import PyMongoError
from html import escape
from flask import current_app, request, jsonify, make_response
from myapp import app

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

@app.route("/createUser", methods=["POST"])
def create_user():
    try:
        db = current_app.config["db"]
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        confirm_password = request.json.get("confirmPassword")
        #Trimming the whitespace and sanitising the input
        username = escape(username.strip())
        email = escape(email.strip())
        password = escape(password.strip())
        confirm_password = escape(confirm_password.strip())
        # Data Validation
        if username == "" or email == "" or password == "":
            return make_response(jsonify(error="All fields are required"), 400)
        if password != confirm_password:
            return make_response(jsonify(error="Passwords do not match"), 400)
        if db.Users.count_documents({"email":email}) > 0:
            return make_response(jsonify(error="Email already in use"), 400)
        if db.Users.count_documents({"username":username}) > 0:
            return make_response(jsonify(error="Username already in use"), 400)
        if len(password) < 8:
            return make_response(jsonify(error="Password must be at least 8 characters"), 400)
        match = re.match(r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$", email)
        if match is None:
            return make_response(jsonify(error="Invalid email"), 400)
        # Hashing the password
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        # Inserting the User into MongDB
        result = db.Users.insert_one({"username": username, "email": email, "password": password_hash})
        return "User created successfully", 200
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)

@app.route("/login",methods=["POST"])
def login_user():
    try:
        db = current_app.config["db"]
        db_users = db["Users"]
        username = request.json.get("username")
        password = request.json.get("password")
        username = username.strip()
        password = password.strip()
        # Data Validation
        user = db_users.find_one({"username":username})
        if user is None:
            return make_response(jsonify(error="Username not found"), 404)
        else:
            stored_password = user["password"]
            if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                #Create JWT for user
                token = jwt.encode({
                    "user_id": str(user["_id"]),
                    "expires": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                },secret_key)
                return make_response(jsonify(success="Logged In successfully"), 200)
            else:
                return make_response(jsonify(error="Invalid Password"), 401)
    except Exception as e:
        return make_response(jsonify(error=str(e)), 500)
