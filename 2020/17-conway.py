import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/17-input.txt').read()

data = {(i, j, 0, 0) for i, row in enumerate(data.splitlines()) for j, d in enumerate(row) if d == '#'}

def gnns(p):
    return [(p[0] + i, p[1] + j, p[2] + k, p[3] + l) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) for l in (-1, 0, 1) if (i, j, k, l) != (0, 0, 0, 0)]

def print_it(data):
    "Print 3D slice with w = 0"
    min_p = tuple(min(data, key=lambda t:t[i])[i] for i in range(3))
    max_p = tuple(max(data, key=lambda t:t[i])[i] for i in range(3))
    for z in range(min_p[2], max_p[2]+1):
        print(f'z = {z}')
        print('\n'.join(''.join('#' if (i, j, z) in data else '.' for j in range(min_p[1], max_p[1] + 1)) for i in range(min_p[0], max_p[0]+1)))

for _ in range(6):
    counts = Counter(nn for p in data if (nns := gnns(p)) for nn in nns)
    data = {p for p, c in counts.items() if (p in data and c == 2) or (c == 3)}

print(len(data))

