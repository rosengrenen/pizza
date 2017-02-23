from flask import Flask
from pizza import *
import json

app = Flask(__name__)

# Render a Pizza python object as a json-formatted string
def json_pizza(pizza):
    clos = pizza.get_closest()
    ret = {
        "name": pizza.name,
        "ingredients": pizza.get_ingredients(),
        "closest": {
            "name": clos.name,
            "ingredients": clos.get_ingredients(),
            "added": clos.get_added(),
            "removed": clos.get_removed()
        }
    }
    return json.dumps(ret)

def print_list(l):
    ret = "<ul>"
    for i in l:
        ret += "<li>" + i + "</li>"
    ret += "</ul>"
    return ret

# Render a Pizza python object as a html-formatted string
def html_pizza(pizza):
    clos = pizza.get_closest()
    ret = "<h1>Name: " + pizza.name + "</h1>"
    ret += "<ul>"
    ret += print_list(pizza.get_ingredients())
    ret += "</ul>"
    ret += "<h1>How to order</h1>"
    ret += "<h2>Ask for: " + pizza.closest.name + "</h2>"
    if clos.get_ingredients() is not None:
        ret += "<h3>It contains</h3>" + print_list(clos.get_ingredients())
    if clos.get_added() is not None:
        ret += "<h3>Add</h3>" + print_list(clos.get_added())
    if clos.get_removed() is not None:
        ret += "<h3>Remove</h3>" + print_list(clos.get_removed())
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

@app.route("/maintainers")
def maintainers():
    return "Frontend Heroes/IO"

if __name__ == "__main__":
    app.run()
