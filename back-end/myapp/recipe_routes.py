# Standard library imports
from bson import ObjectId, json_util
from bson.errors import InvalidId

# Third party imports
from flask import current_app, request, jsonify, make_response
from pymongo.errors import PyMongoError
from recipe_scrapers import scrape_me
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local application imports
from myapp import app

# TODO:
# The results/search only returns recipes from a users collection, as intended!
# The delete button is only visible in view_all if teh recipe is associated with a  user
# to be changed to be a button for adding a recipe into a users collection
# add/create a dashboard for users to be redirected to after logging in displaying 
# their recipes and teh add recipe functionality
# Start testing suite for backend

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
@jwt_required()
def add_recipe():
    try:
        # Get the user_id from the JWT
        user_id = get_jwt_identity()
        
        db = current_app.config["db"]
        # Get URL from request body
        url = request.json.get("url")
        # Check if url is a string
        if not isinstance(url, str):
            return make_response(jsonify(error="URL should be a string"), 400)

        # scrape the recipe
        scraper = scrape_me(url)

        # create dict to store recipe data
        recipe = {
            "name": scraper.title(),
            "total_time": scraper.total_time(),
            "image_url": scraper.image(),
            "ingredients": scraper.ingredients(),
            "instructions": scraper.instructions().split("\n"),
            "users_added": [user_id],
        }

        # Check if recipe already exists
        existing_recipe = db.Recipes.find_one({"name": recipe["name"]})

        if existing_recipe:
            db.Recipes.update_one(
                {"_id": existing_recipe["_id"]},
                {"$addToSet":{"users_added": user_id}}
            )
            return "User added to existing recipe", 200
        else:
            # Insert recipe to mongoDB collection
            recipe["users_added"] = [user_id]
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
@jwt_required()
def delete_recipe():
    try:
        user_id = get_jwt_identity()

        db = current_app.config["db"]
        recipe_id = request.json.get("_id")
        recipe_id = ObjectId(recipe_id)

        recipe = db.Recipes.find_one({"_id": recipe_id})

        if not recipe:
            return make_response(jsonify(error="No recipe found with that _id"), 404)
        
        if user_id not in recipe["users_added"]:
            return make_response(jsonify(error="User did not add this recipe"), 403)
        
        if len(recipe["users_added"]) > 1:
            db.Recipes.update_one(
                {"_id": recipe_id},
                {"$pull": {"users_added": user_id}}
            )
            return "Recipe removed from user's selection", 200
        else:
            result = db.Recipes.delete_one({"_id": recipe_id})
            return "Recipe deleted successfully", 200

    except TypeError:
        return make_response(jsonify(error="Invalid request body"), 400)
    except InvalidId:
        return make_response(jsonify(error="Invalid recipe ID"), 400)
    except PyMongoError as e:
        return make_response(jsonify(error=str(e)), 500)


@app.route("/search", methods=["POST"])
@jwt_required()
def search_recipe():
    try:
        user_id = get_jwt_identity()

        db = current_app.config["db"]
        # Parse teh request body
        ingredients = request.json["ingredients"]
        # create the query for MongoDB
        
        query = {"$text": {"$search": " ".join(ingredients)},"users_added": user_id}
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
