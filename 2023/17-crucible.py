"""
Multiverse Dijkstra. You find all reachable nodes from your current location,
and you need a seperate node for both orientations.

I added a heuristic after to see what the performance difference was and it was
negligble.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter, defaultdict
from itertools import (
    combinations_with_replacement,
    cycle,
    chain,
    repeat,
    islice,
    combinations,
    count,
)
from math import lcm
import functools
import sys
from heapq import heappop, heappush


data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/17/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)


def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tmul(s, b):
    return tuple(s * y for y in b)


def heur(p):
    H, W = len(data), len(data[0])
    return H - p[0] + W - p[1] - 2


grid = {(i, k): int(e) for i, r in enumerate(data) for k, e in enumerate(r)}
H, W = len(data), len(data[0])
target = ((H - 1), (W - 1))
visited = set()
toVisit = [(heur((0,0)), (0, 0), (0, 1)), (heur((0,0)), (0, 0), (1, 0))]

while toVisit:
    h, p, d = heappop(toVisit)
    if p == target:
        print(h)
        break
    if (p, d) in visited:
        continue
    visited.add((p, d))
    h -= heur(p)

    for o in [-1, 1]:
        heat = h
        newp = p
        for _ in range(3):
            newp = tadd(newp, tmul(o, d))
            if newp not in grid:
                break
            heat += grid[newp]
        for _ in range(3, 10):
            newp = tadd(newp, tmul(o, d))
            if newp not in grid:
                break
            heat += grid[newp]
            heappush(toVisit, (heat + heur(newp), newp, (d[1], d[0])))
