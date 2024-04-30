from recipe_scrapers import scrape_me
from pymongo import MongoClient
import json

mongo_connection_str = "mongodb+srv://bradleyhill:YDBJrnsC7CG8WzXg@testrecipesuggestions.mtjmyrr.mongodb.net/?retryWrites=true&w=majority&appName=testRecipeSuggestions"

client = MongoClient(mongo_connection_str)

db = client["testRecipeSuggestions"]
collection = db["Recipes"]

scraper = scrape_me(
    "https://www.bbcgoodfood.com/recipes/chorizo-mozzarella-gnocchi-bake"
)

# print("Host:", scraper.host())
# print("\nTitle:", scraper.title())
# print("\nTotal Time:", scraper.total_time())
# print("\nImage URL:", scraper.image())

# print("\nIngredients:")
# for ingredient in scraper.ingredients():
#     print("  -", ingredient)

# print("\nIngredient Groups:")
# for group in scraper.ingredient_groups():
#     print("  -", group)

# print("\nInstructions:")
# for instruction in scraper.instructions().split("\n"):
#     print("  -", instruction)


ingredients = scraper.ingredients()
ingredients_json = json.dumps(ingredients)

print(ingredients_json)

collection.insert_one({"ingredients": ingredients_json})
