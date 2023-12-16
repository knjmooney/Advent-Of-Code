"""
A bit of a silly solution. Just playing around with pattern matching.
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

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/16/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

U = (-1, 0)
D = (1, 0)
L = (0, -1)
R = (0, 1)

visited = set()
grid = {(i, j): e for i, r in enumerate(data) for j, e in enumerate(r)}

def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def go(p):
    dir, pos = p
    if pos not in grid or p in visited:
        return
    visited.add(p)
    match (dir, grid[pos]):
        case (_, "/"):
            dir = (-dir[1], -dir[0])
            go((dir, tadd(pos, dir)))
        case (_, "\\"):
            dir = (dir[1], dir[0])
            go((dir, tadd(pos, dir)))
        case [(0, 1), "|"] | [(0, -1), "|"]:
            go((U, pos))
            go((D, pos))
        case ((1, 0), "-") | ((-1, 0), '-'):
            go((L, pos))
            go((R, pos))
        case (_, _):
            go((dir, tadd(pos, dir)))

sys.setrecursionlimit(10000)
result = 0
H = len(data) - 1
for dir in [L, R, U, D]:
    for i in range(len(data)):
        for p in [(i, 0), (i, H), (0, i), (H, i)]:
            visited.clear()
            go((dir, p))
            result = max(result, len(set(p for _, p in visited)))

print(result)