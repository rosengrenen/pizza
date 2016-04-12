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

@app.route("/")
def veg_pizza():
    return json_pizza([])

@app.route("/meat")
def meat_pizza():
    return json_pizza(["meat"])

if __name__ == "__main__":
    app.run()
