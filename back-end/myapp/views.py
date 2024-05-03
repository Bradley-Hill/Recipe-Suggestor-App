from myapp import app, mongo
from flask import request, json, abort
from recipe_scrapers import scrape_me
from bson.json_util import dumps


@app.route("/add", methods=["POST", "OPTIONS"])
def add_recipe():
    if request.method == "OPTIONS":
        return ("", 204)
    elif request.method == "POST":

        # Get URL from request body
        url = request.json["url"]

        # scrape the recipe
        scraper = scrape_me(url)

        # create dict to store recipe data
        recipe = {
            "name": scraper.title(),
            "total_time": scraper.total_time(),
            "image_url": scraper.image(),
            "ingredients": scraper.ingredients(),
            "instructions": scraper.instructions().split("\n"),
        }

        # Insert recipe to mongoDB collection
        mongo.db.recipes.insert_one(recipe)

    return "Recipe added successfully", 200


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
