from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = (
    "mongodb+srv://bradleyhill:YDBJrnsC7CG8WzXg@testrecipesuggestions.mtjmyrr.mongodb.net/?retryWrites=true&w=majority&appName=testRecipeSuggestions"
)
mongo = PyMongo(app)
