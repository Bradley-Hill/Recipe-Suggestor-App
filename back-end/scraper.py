import json
from recipe_scrapers import scrape_me
from pymongo import MongoClient

# Creating mongoDB connection
mongo_connection_str = "mongodb+srv://bradleyhill:YDBJrnsC7CG8WzXg@testrecipesuggestions.mtjmyrr.mongodb.net/?retryWrites=true&w=majority&appName=testRecipeSuggestions"
client = MongoClient(mongo_connection_str)

# Accessing the database and Recipes collection
db = client["testRecipeSuggestions"]
collection = db["Recipes"]

# Inserting document into collection(Create operation)
scraper = scrape_me("https://www.bbcgoodfood.com/recipes/paprika-pork")
ingredients = scraper.ingredients()
ingredients_json = json.dumps(ingredients)
collection.insert_one({"ingredients": ingredients_json})

# Find a single document in teh collection(Read operation)
query = {"ingredients": json.dumps(["pork"])}
doc = collection.find_one(query)
print(doc)

# Updating a document in the collection(Update operation)
new_values = {"$set": {"ingredients": json.dumps(["Manna from Heaven"])}}
collection.update_one(query, new_values)

# Deleting a document from the collection (Delete operation)
collection.delete_one(query)
