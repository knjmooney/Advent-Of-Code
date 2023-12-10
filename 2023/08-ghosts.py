'''

'''

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import combinations_with_replacement, cycle, chain, repeat, islice
from math import lcm

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/8/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode().splitlines()
)

dirs = data[0]

data = [parse('{} = ({}, {})', d).fixed for d in data[2:]]
maps = {a : (b, c) for a, b, c in data}

nodes = [node for node in maps if node.endswith('A')]

def findZs(node):
    step = 0
    for i, dir in cycle(enumerate(dirs)):
        if node.endswith('Z'):
            return step
        l, r = maps[node]
        if dir == 'L':
            node = l
        elif dir == 'R':
            node = r
        step += 1

muls = [findZs(node) for node in nodes]
print(muls)
print([mul/283 for mul in muls])
print(lcm(*muls))