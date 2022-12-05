"""
Pretty slow as it is. Writing a generator function for integer partitions would make it faster.
"""

from collections import namedtuple
from distutils.errors import DistutilsClassError
from itertools import combinations, combinations_with_replacement, groupby, permutations, product
from time import sleep
from exceptiongroup import catch
from matplotlib.pyplot import text
from requests_cache import CachedSession
from parse import parse, findall
from pprint import pprint
import json
import re

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/15/input', cookies=cookies)
    .content
    .strip()
    .decode()
    .splitlines()
)

# data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".splitlines()

data = [
    parse('{name}: capacity {capacity:d}, durability {durability:d}, flavor {flavor:d}, texture {texture:d}, '
          'calories {calories:d}', d).named
    for d in data
]

def score(perm):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for p, d in zip(perm, data):
        capacity += d['capacity'] * p
        durability += d['durability'] * p
        flavor += d['flavor'] * p
        texture += d['texture'] * p
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0
    return capacity * durability * flavor * texture

def total_calories(perm):
    return sum(d['calories'] * p for p, d in zip(perm, data))

print(max(score(p) for p in product(range(101), repeat=len(data)) if (sum(p) == 100) and total_calories(p) == 500))
