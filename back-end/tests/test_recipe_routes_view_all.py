import pytest
from flask import json, Flask, current_app
from pymongo.errors import PyMongoError, ExecutionTimeout
from myapp import create_app
from unittest.mock import patch, MagicMock
from myapp.recipe_routes import view_all

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

def test_view_all_success(app):
    with app.app_context():
        response = view_all()
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data,list)
        for recipe in data:
            assert isinstance(recipe,dict)
            assert isinstance(recipe["_id"], str)

def test_view_all_db_error(app):
    with app.app_context():
        mock_db = app.config['db']
        with patch.object(mock_db.Recipes, 'find',side_effect=PyMongoError("Database connection error")):
            response = view_all()

            assert response.status_code == 500
            data = response.get_json()
            assert 'error' in data
            assert data['error'] == "Database connection error"

def test_view_all_empty_database(app):
    with app.app_context():
        mock_db = app.config["db"]
        mock_db.Recipes.find.return_value = []

        response = view_all()
        data = response.get_json()
        assert data == [], "Expect an empty list when db is empty"

def test_view_all_data_transformation(app):
    with app.app_context():
        response = view_all()
        recipes = response.get_json()
        for recipe in recipes:
            assert isinstance(recipe['_id'],str),"The _id field must be a string"

def test_view_all_server_timeout(app):
    with app.app_context():
        mock_db = app.config["db"]
        with patch.object(mock_db.Recipes, 'find', side_effect=ExecutionTimeout("Timeout Error")):
            response = view_all()

            assert response.status_code == 500
            data = response.get_json()
            assert 'error' in data
            assert "Timeout Error" in data['error']
