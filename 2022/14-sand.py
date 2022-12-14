'''
Solution takes > 2 seconds on a Mac M1. I've tried a few simple changes to
speed it up, but nothing has been significant enough to justify added 
complexity. One thing that might speed it up would be to use a 2D array
for the board rather than a set.
'''

from collections import defaultdict, deque, namedtuple
from functools import cmp_to_key
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod
from heapq import heappop, heappush

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/14/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .split('\n')
)

data = [[(int(e.split(',')[0]), int(e.split(',')[1])) for e in d.split(' -> ')] for d in data]

walls = set()
for d in data:
    for a, b in zip(d, d[1:]):
        s, e = min(a[0], b[0]), max(a[0], b[0])
        for i in range(s, e+1):
            walls.add((i, a[1]))
        s, e = min(a[1], b[1]), max(a[1], b[1])
        for i in range(s, e+1):
            walls.add((a[0], i))

lowest = max(e[1] for e in walls)
sand = (500, 0)
sands = set()
while sand not in sands:
    open_routes = [n for q in (0, -1, 1) if (n := (sand[0]+q, sand[1]+1)) not in walls]
    if open_routes and not sand[1] == lowest + 1:
        sand = open_routes[0]
    else:
        walls.add(sand)
        sands.add(sand)
        sand = (500, 0)

print(len(sands))