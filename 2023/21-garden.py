"""
Old code, not sure if it works.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter, defaultdict, deque
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
        "https://adventofcode.com/2023/day/21/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

# data = '''...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........'''.splitlines()

U = (-1, 0)
D = (1, 0)
L = (0, -1)
R = (0, 1)


def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tmul(s, b):
    return tuple(s * y for y in b)


def mann(p, q):
    return q[0] - p[0] + q[1] - p[1]


grid = {(i, k): e for i, r in enumerate(data) for k, e in enumerate(r)}
H, W = len(data), len(data[0])
visited = set()
start = next(k for k, v in grid.items() if v == 'S')
toVisit = [start]
nsteps = 130
for _ in range(1 + nsteps):
    toVisitPrev = toVisit
    toVisit = []
    for p in toVisitPrev:
        if p in visited or p not in grid or grid[p] == '#':
            continue
        visited.add(p)
        for d in [U, D, L, R]:
            toVisit.append(tadd(p, d))

print(sum(mann(start, v) % 2 == 0 for v in visited))
# print(visited)
# for v in visited:
# print(visited)