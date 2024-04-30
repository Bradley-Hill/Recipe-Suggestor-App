from myapp import app, mongo


@app.route("/add", methods=["POST"])
def add_recipe():
    # code to add recipe to mongoDB
    pass


@app.route("/search", methods=["GET"])
def search_recipe():
    # code to return a recipe from mongoDB
    pass
