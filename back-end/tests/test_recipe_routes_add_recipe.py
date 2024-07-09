import pytest
from flask import json, Flask, current_app
from flask_jwt_extended import create_access_token
from pymongo.errors import PyMongoError, ExecutionTimeout
from myapp import create_app
from unittest.mock import patch, MagicMock
from myapp.recipe_routes import add_recipe

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    mock_db = MagicMock()

    # mock_db.Recipes.find.return_value = [
    #     {
    #         "_id": "666ac26a5a941dae139ec173",
    #         "name": "Feta & peach couscous",
    #         "total_time": 20,
    #         "image_url": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/fe…",
    #         "ingredients": ["Ingredient 1", "Ingredient 2", "Ingredient 3", "Ingredient 4"],
    #         "instructions": ["Step 1: Do something"],
    #         "users_added": ["User1"]
    #     },
    #     {"_id": "507f1f77bcf86cd799439012", 
    #      "name": "Sausage and Mash",
    #      "total_time":30,
    #      "image_url":"https://images.immediate.co.uk/production/volatile/sites/30/2020/08/re…",
    #      "ingredients":["Ingredient 1","Ingredient 2"],
    #      "instructions":["Step 1: Do something"],
    #      "users_added":["User2"]
    #      }
    # ]

    mock_insert_result = MagicMock()
    mock_insert_result.inserted_id = "new_recipe_id"
    mock_db.Recipes.insert_one.return_value = mock_insert_result

    app.config["db"] = mock_db
    app.add_url_rule('/add_recipe', view_func=add_recipe, methods=['POST'])

    return app

@patch('myapp.recipe_routes.scrape_me')
def test_add_recipe_success(scrape_me,app):
        scrape_me.return_value = {
        "name": "Test Recipe",
        "total_time": 10,
        "image_url": "https://example.com/test_recipe.jpg",
        "ingredients": ["Ingredient A", "Ingredient B"],
        "instructions": ["Step 1: Do something"],
        "users_added": ["User1"]
    }

        test_user_id = 'admin'
        with app.app_context():
            test_token = create_access_token(identity=test_user_id)

        with app.test_client() as client:
            data = {"url":"https://example.com/recipe"}
            headers = {"Authorization": f"Bearer {test_token}"}
            response = client.post('/add_recipe', json=data, headers=headers)

            app.config["db"].Recipes.insert_one.assert_called_with(scrape_me.return_value)
            assert response.status_code == 200