from flask import current_app, request, jsonify
from myapp import app
from recipe_scrapers import scrape_me


@app.route("/")
def index():
    db = current_app.config["db"]
    recipes = db.Recipes.find()
    for recipe in recipes:
        print(recipe)
    return "Check teh console for output"


@app.route("/test")
def test():
    db = current_app.config["db"]
    print(f"Connected to database: {db.name}")
    recipes = db.Recipes.find()
    recipes_list = list(recipes)
    for recipe in recipes_list:
        recipe["_id"] = str(recipe["_id"])
    return jsonify(recipes_list)


@app.route("/add", methods=["POST"])
def add_recipe():
    db = current_app.config["db"]
    # Get URL from request body
    url = request.form.get("url")

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
    result = db.Recipes.insert_one(recipe)
    print(result.inserted_id)

    return "Recipe added successfully", 200


# @app.route("/search", methods=["POST"])
# def search_recipe():
#     # Parse teh request body
#     ingredients = request.json["ingredients"]

#     # Database query
#     recipes = mongo.db.recipes.find()

#     # Convert query result to list of dicts
#     recipes_list = [
#         recipe
#         for recipe in recipes
#         if any(
#             ingredient in json.loads(recipe["ingredients"])
#             for ingredient in ingredients
#         )
#     ]

#     # s Send teh response
#     return dumps(recipes_list), 200
