# User and login/auth routes to be kept here
import re
from flask import current_app, request, jsonify, make_response
from myapp import app

@app.route("/createUser", methods=["POST"])
def create_user():
    try:
        db = current_app.config["db"]
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        confirm_password = request.json.get("confirmPassword")
        # Data Validation
        if password != confirm_password:
            return make_response(jsonify(error="Passwords do not match"), 400)
        if db.Users.find({"email": email}).count() > 0:
            return make_response(jsonify(error="Email already exists"), 400)
        if username == "" or email == "" or password == "":
            return make_response(jsonify(error="All fields are required"), 400)
        if len(password) < 8:
            return make_response(jsonify(error="Password must be at least 8 characters"), 400)
        match = re.match(r"[^@]+@[^@]+\.[^@]+", email)
        if match is None:
            return make_response(jsonify(error="Invalid email"), 400)
