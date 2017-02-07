from flask import Flask
from pizza import *
import json

app = Flask(__name__)

# Render a Pizza python object as a json-formatted string
def json_pizza(pizza):
    ret = {
        "name": pizza.name,
        "ingredients": pizza.get_ingredients()
    }
    ret.update(findClosestPizza(pizza))
    return json.dumps(ret)
# Render a Pizza python object as a html-formatted string
def html_pizza(pizza):
    ret = "<h1>Name: " + pizza.name + "</h1>"
    ret += "<ul>"
    for i in pizza.get_ingredients():
        ret += "<li>" + i + "</li>"
    ret += "</ul>"
    return ret

@app.route("/")
def html_veg_pizza():
    pizza = random_pizza()
    return html_pizza(pizza)

@app.route("/meat")
def html_meat_pizza():
    pizza = random_pizza(["meat"])
    return html_pizza(pizza)

@app.route("/json")
def veg_pizza():
    pizza = random_pizza()
    return json_pizza(pizza)

@app.route("/json/meat")
def meat_pizza():
    pizza = random_pizza(["meat"])
    return json_pizza(pizza)

if __name__ == "__main__":
    app.run()
