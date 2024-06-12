# Standard library imports
from bson import ObjectId, json_util
from bson.errors import InvalidId

# Third party imports
from flask import current_app, request, jsonify, make_response
from jwt import InvalidTokenError, ExpiredSignatureError
from pymongo.errors import PyMongoError
from recipe_scrapers import scrape_me

# Local application imports
from myapp import app
import jwt


@app.route("/view_all", methods=["GET"])
def view_all():
    try:

        db = current_app.config["db"]
        recipes = db.Recipes.find()
        recipes_list = list(recipes)
        for recipe in recipes_list:
            recipe["_id"] = str(recipe["_id"])
        return jsonify(recipes_list)
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)


@app.route("/add", methods=["POST"])
def add_recipe():
    try:
        if "Authorization" not in request.headers:
            return make_response(jsonify(error="Missing Authorization header"), 401)
        try:
            decoded_jwt = jwt.decode(request.headers["Authorization"], current_app.config["SECRET_KEY"], algorithms=["HS256"])
        except InvalidTokenError:
            return make_response(jsonify(error="Invalid token"), 401)
        except ExpiredSignatureError:
            return make_response(jsonify(error="Token has expired"), 401)
        
        db = current_app.config["db"]
        # Get URL from request body
        url = request.json.get("url")

        # scrape the recipe
        scraper = scrape_me(url)

        # create dict to store recipe data
        recipe = {
            "name": scraper.title(),
            "total_time": scraper.total_time(),
            "image_url": scraper.image(),
            "ingredients": scraper.ingredients(),
            "instructions": scraper.instructions().split("\n"),
            "users_added": [decoded_jwt["username"]],
        }

        # Check if recipe already exists
        existing_recipe = db.Recipes.find_one({"name": recipe["name"]})

        if existing_recipe:
            db.Recipes.update_one(
                {"_id": existing_recipe["_id"]},
                {"$addToSet":{"users_added": decoded_jwt["user_id"]}}
            )
            return "User added to existing recipe", 200
        else:
            # Insert recipe to mongoDB collection
            recipe["users_added"] = [decoded_jwt["user_id"]]
            db.Recipes.insert_one(recipe)
            return "Recipe added succesfully", 200
    except TypeError:
        return make_response(jsonify(error="Invalid request body"), 400)
    except InvalidId:
        return make_response(jsonify(error="Invalid recipe ID"), 400)
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)

    return "Recipe added successfully", 200


@app.route("/delete_recipe", methods=["DELETE"])
def delete_recipe():
    try:
        db = current_app.config["db"]
        recipe_id = request.json.get("_id")
        recipe_id = ObjectId(recipe_id)
        result = db.Recipes.delete_one({"_id": recipe_id})
        if result.deleted_count == 0:
            return make_response(jsonify(error="No recipe found with that _id"), 404)
        return "Recipe deleted successfully", 200
    except TypeError:
        return make_response(jsonify(error="Invalid request body"), 400)
    except InvalidId:
        return make_response(jsonify(error="Invalid recipe ID"), 400)
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)


@app.route("/search", methods=["POST"])
def search_recipe():
    try:
        db = current_app.config["db"]
        # Parse teh request body
        ingredients = request.json["ingredients"]
        # create the query for MongoDB
        #
        query = {"$text": {"$search": " ".join(ingredients)}}
        # execute teh query
        cursor = db.Recipes.find(query)
        # List of recipes from query
        found_recipes = list(cursor)

        found_recipes_json = json_util.dumps(found_recipes)

        return found_recipes_json
    except TypeError:
        return make_response(jsonify(error="Invalid request body"), 400)
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)
