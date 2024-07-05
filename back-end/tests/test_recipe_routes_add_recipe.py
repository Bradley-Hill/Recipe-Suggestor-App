import pytest
from flask import json, Flask, current_app
from pymongo.errors import PyMongoError, ExecutionTimeout
from myapp import create_app
from unittest.mock import patch, MagicMock
from myapp.recipe_routes import add_recipe

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    mock_db = MagicMock()
    mock_db.Recipes.find.return_value = [
        {
            "_id": "666ac26a5a941dae139ec173",
            "name": "Feta & peach couscous",
            "total_time": 20,
            "image_url": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/fe…",
            "ingredients": ["Ingredient 1", "Ingredient 2", "Ingredient 3", "Ingredient 4"],
            "instructions": ["Step 1: Do something"],
            "users_added": ["User1"]
        },
        {"_id": "507f1f77bcf86cd799439012", 
         "name": "Sausage and Mash",
         "total_time":30,
         "image_url":"https://images.immediate.co.uk/production/volatile/sites/30/2020/08/re…",
         "ingredients":["Ingredient 1","Ingredient 2"],
         "instructions":["Step 1: Do something"],
         "users_added":["User2"]
         }
    ]
    app.config["db"] = mock_db
    return app