import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod, sqrt
from bisect import bisect_left, insort
from copy import deepcopy
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/18-input.txt').read().splitlines()

def add_ids(node, curr):
    if isinstance(node[0], int):
        a = [(curr + (0,), node[0])]
    else:
        a = add_ids(node[0], curr + (0,))
    if isinstance(node[1], int):
        b = [(curr + (1,), node[1])]
    else:
        b = add_ids(node[1], curr + (1,))
    return a + b

def update(data, id, value):
    node = data[id[0]]
    for i in id[1:-1]:
        node = node[i]
    node[id[-1]] = node[id[-1]] + value

def explode(data, ids, a, b):
    id = a[0][:-1]
    assert a[0][:-1] == b[0][:-1]
    assert len(id) == 4

    node = data[id[0]]
    for i in id[1:]:
        node = node[i]

    i = ids.index(a)
    if i > 0:
        update(data, ids[i - 1][0], a[1])
    if i < len(ids) - 2:
        update(data, ids[i + 2][0], b[1])

    data[id[0]][id[1]][id[2]][id[3]] = 0

def split(data, a):
    id = a[0]
    v = a[1]
    node = data
    for i in id[:-1]:
        node = node[i]
    node[id[-1]] = [v // 2, v // 2 + v%2]

def process(data):
    ids = add_ids(data, tuple())
    to_explode = [id for id in ids if len(id[0]) >= 5]
    to_split = [id for id in ids if id[1] >= 10]
    assert len(to_explode) % 2 == 0
    while to_explode or to_split:
        while to_explode:
            a = to_explode[0]
            b = to_explode[1]
            explode(data, ids, a, b)
            ids = add_ids(data, tuple())
            to_explode = [id for id in ids if len(id[0]) >= 5]
        to_split = [id for id in ids if id[1] >= 10]
        if to_split:
            a = to_split[0]
            split(data, a)
        ids = add_ids(data, tuple())
        to_explode = [id for id in ids if len(id[0]) >= 5]
        to_split = [id for id in ids if id[1] >= 10]

    return data

def magnitude(node):
    if isinstance(node, int):
        return node
    return 3 * magnitude(node[0]) + 2 * magnitude(node[1])


data = [eval(d) for d in data]
result = process(deepcopy(data[0]))
for line in data[1:]:
    result = process([deepcopy(result)] + [deepcopy(line[:])])
print(magnitude(result))

magnitudes = []
for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            continue
        magnitudes.append(magnitude(process([deepcopy(data[i])] + [deepcopy(data[j])])))

print(max(magnitudes))