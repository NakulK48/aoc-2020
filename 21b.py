from copy import copy
from collections import defaultdict
import re

line_regex = re.compile(r"(.*) \(contains (.*)\)")

with open("21.txt") as file_obj:
    lines = [line.strip("\n") for line in file_obj.readlines()]

parsed = []
ingredients_by_allergen = {}

for line in lines:
    [(ingredient_string, allergen_string)] = line_regex.findall(line)
    ingredients = set(ingredient_string.split(" "))
    allergens = allergen_string.split(", ")
    parsed.append((ingredients, allergens))

for ingredients, allergens in parsed:
    for allergen in allergens:
        if allergen not in ingredients_by_allergen:
            ingredients_by_allergen[allergen] = copy(ingredients)
        else:
            ingredients_by_allergen[allergen] &= ingredients

allergen_and_ingredient = []
used = set()

while True:
    if len(allergen_and_ingredient) == len(ingredients_by_allergen):
        break
    for allergen, ingredients in ingredients_by_allergen.items():
        possible = ingredients - used
        if len(possible) == 1:
            ingredient = next(iter(possible))
            allergen_and_ingredient.append((allergen, ingredient))
            used.add(ingredient)

allergen_and_ingredient.sort()
ingredients_sorted = [ing for allerg, ing in allergen_and_ingredient]
print(",".join(ingredients_sorted))
