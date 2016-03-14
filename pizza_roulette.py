#!/usr/bin/env python

import codecs
import random
import os
import sys

# Picks an element at random from 'possibilities' and add it to 'picked'. Keep 
# trying to pick until an item that isn't already in picked appears, thereby
# eliminating duplicates
def pickFrom(possibilities, picked):
    select = random.randint(0, len(possibilities) -1)
    while possibilities[select] in picked:
        select = random.randint(0, len(possibilities) -1)
    picked.append(possibilities[select])

# Returns a list of items by opening the given file (filename given relative to 
# directory of script) and reading items, splitting by lines
def addIngredients(filename):
    dirname = os.path.dirname(os.path.realpath(__file__))
    filename = dirname + filename
    with open(filename) as ingredients:
        ret = ingredients.read().splitlines()
    return ret

# The max and minimum number of ingredients, not counting sauces
MIN_INGRED = 2
MAX_INGRED = 6

# Load all basic ingredients
ingredients = addIngredients("/vegetarian")

# If specified on command line, load meat as well
if "meat" in sys.argv :
    ingredients = ingredients + addIngredients("/meat")

# The list to return
roulette_result = []

# The number of ingredients we will add
roulette_tries = random.randint(MIN_INGRED,MAX_INGRED)

# The number of sauces to put on the pizza
sauces_nbr = random.randint(0,2)

# Add as many ingredients as roulette_tries specified
for i in range(0, roulette_tries):
    pickFrom(ingredients, roulette_result)

# Add as many sauces as sauces_nbr specified
sauces = addIngredients("/sauce")
for i in range(0, sauces_nbr):
    pickFrom(sauces, roulette_result)

# Print the results
for string in roulette_result:
    print string.decode('utf-8', 'ignore')

