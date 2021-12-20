import re
import os
from collections import Counter, defaultdict, namedtuple
from itertools import combinations, product
from pprint import pprint
from parse import parse, findall
from math import prod, sqrt
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/21-input.txt').read().splitlines()
data = [parse('{} (contains {})', d).fixed for d in data]
data = [(set(i.split(' ')), a.split(', ')) for i, a in data]
set_of_all_ingredients = set.union(*[i for i, _ in data])
all_ingredients = sum((list(i) for i, _ in data), list())

result = dict()
for ingredients, allergens in data:
    for allergen in allergens:
        if allergen in result:
            result[allergen] &= ingredients
        else:
            result[allergen] = ingredients.copy()

set_of_ingredients_with_no_allergens = set_of_all_ingredients.copy()
for allergen, ingredients in result.items():
    set_of_ingredients_with_no_allergens -= ingredients

print(sum([all_ingredients.count(s) for s in set_of_ingredients_with_no_allergens]))

result2 = {}
allergens_left = list(result.keys())
ingredients_identified = set()
while allergens_left:
    for allergen in allergens_left.copy():
        possibles = result[allergen] - ingredients_identified
        if len(possibles) == 1:
            ingredient = possibles.pop()
            result2[allergen] = ingredient
            ingredients_identified.add(ingredient)
            allergens_left.remove(allergen)

print(','.join(result2[allergen] for allergen in sorted(result2.keys())))
