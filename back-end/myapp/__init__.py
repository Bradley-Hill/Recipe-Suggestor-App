from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_cors import CORS

print("MongDB client init...")
app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = (
    "mongodb+srv://bradleyhill:YDBJrnsC7CG8WzXg@testrecipesuggestions.mtjmyrr.mongodb.net/?retryWrites=true&w=majority&appName=testRecipeSuggestions"
)

mongo = PyMongo(app)

print(mongo.db)
