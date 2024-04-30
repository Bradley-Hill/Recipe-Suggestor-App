from myapp import app, mongo
from flask import request, json
from bson.json_util import dumps


@app.route("/add", methods=["POST"])
def add_recipe():
    # code to add recipe to mongoDB
    pass


@app.route("/search", methods=["POST"])
def search_recipe():
    # Parse teh request body
    ingredients = request.json["ingredients"]

    # Database query
    recipes = mongo.db.recipes.find()

    # Convert query result to list of dicts
    recipes_list = [
        recipe
        for recipe in recipes
        if any(
            ingredient in json.loads(recipe["ingredients"])
            for ingredient in ingredients
        )
    ]

    # s Send teh response
    return dumps(recipes_list), 200
