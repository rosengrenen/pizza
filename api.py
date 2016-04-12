from flask import Flask
from pizza import random_pizza

app = Flask(__name__)

def json_pizza(pizza_args):
    pizza = random_pizza(pizza_args)
    ret = "{"
    ret += "\"name\":\"" + pizza.name + "\", "
    ret += "\"ingredients\":["
    ingredients = []
    for i in pizza.ingredients:
        ingredients.append("\"" + i + "\"")
    ret += ", ".join(ingredients)
    ret += "]"
    ret += "}"
    return ret

def html_pizza(pizza):
    ret = "<h1>Name: " + pizza.name + "</h1>"
    ret += "<ul>"
    for i in pizza.ingredients:
        ret += "<li>" + i + "</li>"
    ret += "</ul>"
    return ret

@app.route("/")
def html_veg_pizza():
    pizza = random_pizza([])
    return html_pizza(pizza)

@app.route("/meat")
def html_meat_pizza():
    pizza = random_pizza(["meat"])
    return html_pizza(pizza)

@app.route("/json")
def veg_pizza():
    return json_pizza([])

@app.route("/json/meat")
def meat_pizza():
    return json_pizza(["meat"])

if __name__ == "__main__":
    app.run()
