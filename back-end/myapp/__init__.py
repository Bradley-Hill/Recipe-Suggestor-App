from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

print("MongDB client init...")
app = Flask(__name__)
CORS(app)

mongo_connection_str = "mongodb+srv://bradleyhill:YDBJrnsC7CG8WzXg@testrecipesuggestions.mtjmyrr.mongodb.net/?retryWrites=true&w=majority&appName=testRecipeSuggestions"
client = MongoClient(mongo_connection_str)

db = client["testRecipeSuggestions"]
app.config["db"] = db

import myapp.views
