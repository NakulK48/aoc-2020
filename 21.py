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

allergen_ingredients = set()
for ing_set in ingredients_by_allergen.values():
    allergen_ingredients |= ing_set

result = sum(
    len(ingredients - allergen_ingredients) for ingredients, _ in parsed
)

print(result)
