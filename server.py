from flask import Flask, request, abort
import json
from config import me, db
from mock_data import catalog

app = Flask("Server")


@app.get("/")
def home():
    return "Hello from flask"


@app.get("/test")
def test():
    return "This is a test"


@app.get("/about")
def about():
    return "Blake Spears"

################################################################
# API ENDPOINTS
# JSON
################################################################


@app.get("/api/version")
def version():
    v = {
        "version": "1.0.0",
        "build": "42",
        "name": "sloth",
        "developer": me
    }

    return json.dumps(v)


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


@app.post("/api/catalog")
def save_product():
    product = request.get_json()

    if product is None:
        return abort(400, "Product required")

    db.products.insert_one(product)
    print("-----------------------")
    print(product)
    print("--------------------------")
    
    return json.dumps(product)


@app.get("/api/products/count")
def total_price():
    total = 0
    for prod in catalog:
        total += prod["price"]
    return json.dumps(total)


@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    for prod in catalog:
        if prod["category"].lower() == category.lower():
            results.append(prod)

    return json.dumps(results)


@app.get("/api/catalog/lower/<amount>")
def lower_than(amount):
    results = []
    for prod in catalog:
        if prod["price"] < float(amount):
            results.append(prod)

    return json.dumps(results)


@app.get("/api/category/unique")
def unique_cats():
    results = []
    for prod in catalog:
        category = prod["category"]
        if not category in results:
            results.append(prod["category"])

    return json.dumps(results)


@app.get("/api/test/colors")
def unique_colors():
    colors = ["red", 'blue', "Pink", "yelloW", "Red",
              "Black", "BLUE", "RED", "BLACK", "YELLOW"]
    results = []
    for color in colors:
        color = color.lower()
        if not color in results:
            results.append(color)

    return json.dumps(results)


@app.get("/api/test/count/<color>")
def count_color(color):
    color = color.lower()
    colors = ["red", 'blue', "Pink", "yelloW", "Red",
              "Black", "BLUE", "RED", "BLACK", "YELLOW"]
    count = 0
    for item in colors:
        if color == item.lower():
            count += 1

    return json.dumps(count)


# app.run(debug=True)
