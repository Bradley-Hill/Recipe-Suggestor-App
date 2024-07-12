import pytest
from flask import json, Flask, current_app
from flask_jwt_extended import create_access_token, JWTManager,jwt_required
from pymongo.errors import PyMongoError, ExecutionTimeout
from dotenv import load_dotenv
import os
from myapp import create_app
from unittest.mock import patch, MagicMock
from myapp.recipe_routes import add_recipe
from recipe_scrapers import scrape_me

@pytest.fixture
def app():
    load_dotenv()
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
    JWTManager(app)
    mock_db = MagicMock()

    mock_insert_result = MagicMock()
    mock_insert_result.inserted_id = "new_recipe_id"
    mock_db.Recipes.insert_one.return_value = mock_insert_result

    app.config["db"] = mock_db
    app.add_url_rule('/add_recipe', view_func=add_recipe, methods=['POST'])

    return app

@patch('myapp.recipe_routes.scrape_me')
def test_add_recipe_success(scrape_me_mock, app):
    
    scraper_mock = MagicMock()
    scraper_mock.title.return_value = "Test Recipe"
    scraper_mock.total_time.return_value = 10
    scraper_mock.image.return_value = "https://example.com/test_recipe.jpg"
    scraper_mock.ingredients.return_value = ["Ingredient A", "Ingredient B"]
    scraper_mock.instructions.return_value = "Step 1: Do something"

    # Set the return value of scrape_me to the mock scraper object
    scrape_me_mock.return_value = scraper_mock

    test_user_id = 'admin'
    with app.app_context():
        test_token = create_access_token(identity=test_user_id)

        with app.test_client() as client:
            data = {"url":"https://example.com/recipe"}
            headers = {"Authorization": f"Bearer {test_token}"}
            response = client.post('/add_recipe', json=data, headers=headers)

            # app.config["db"].Recipes.insert_one.assert_called_with(scrape_me.return_value)
            assert response.status_code == 200

            assert response.data.decode('utf-8') in ["User added to existing recipe","Recipe added successfully"]

            scrape_me_mock.assert_called_once_with("https://example.com/recipe")

