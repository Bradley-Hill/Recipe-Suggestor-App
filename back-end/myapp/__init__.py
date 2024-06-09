from flask import Flask
from pymongo import MongoClient
from pymongo import TEXT
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

print("MongDB client init...")
app = Flask(__name__)
CORS(app)

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
