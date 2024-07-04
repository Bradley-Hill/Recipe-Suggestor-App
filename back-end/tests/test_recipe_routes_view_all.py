import pytest
from flask import json, Flask, current_app
from pymongo.errors import PyMongoError
from myapp import create_app
from unittest.mock import patch, MagicMock
from myapp.recipe_routes import view_all

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    mock_db = MagicMock()
    mock_db.Recipes.find.return_value = [
        {"_id": "507f1f77bcf86cd799439011", "name": "Test Recipe 1"},
        {"_id": "507f1f77bcf86cd799439012", "name": "Test Recipe 2"}
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

    assert response.status_code == 200