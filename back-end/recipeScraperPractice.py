import json
from recipe_scrapers import scrape_me


scraper = scrape_me("https://www.bbcgoodfood.com/recipes/paprika-pork")

print("Host:", scraper.host())
print("\nTitle:", scraper.title())
print("\nTotal Time:", scraper.total_time())
print("\nImage URL:", scraper.image())

print("\nIngredients:")
for ingredient in scraper.ingredients():
    print("  -", ingredient)

print("\nIngredient Groups:")
for group in scraper.ingredient_groups():
    print("  -", group)

print("\nInstructions:")
for instruction in scraper.instructions().split("\n"):
    print("  -", instruction)
