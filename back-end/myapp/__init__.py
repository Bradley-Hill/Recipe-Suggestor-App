from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo import TEXT
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

load_dotenv()

print("MongDB client init...")
app = Flask(__name__)
CORS(app)

#Setting secret key for JWT here
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback(jwt_header,jwt_payload):
    return jsonify({"message":"Token has expired"}), 401

mongo_connection_str = os.getenv("MONGO_CONNECTION_STR")
client = MongoClient(mongo_connection_str)

db = client["testRecipeSuggestions"]

# ensure that the Recipes collection has text index assigned to "ingredients" field for search
indexes = db["Recipes"].list_indexes()
if not any(index["name"] == "ingredients_text" for index in indexes):
    db["Recipes"].create_index([("ingredients", TEXT)])

app.config["db"] = db

import myapp.recipe_routes
import myapp.user_routes
