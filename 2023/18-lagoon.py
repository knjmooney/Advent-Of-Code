"""
Pick's theorem, for polygon's with integer vertices, states

  A = i + b / 2 - 1

where A is total area, i is the number of enclosed points, b is the number of
points touching a boundary.

The shoelace theorem is a formula for calculating the area of a polygon

  A = 1/2 \sum_j (y[j] + y[j+1]) * (x[j] - x[j+1])

The answer to our problem isn't the area of the enclosed polygon (consider R 1,
D 1, L 1, U 1), it's the area of a slightly larger polygon given by

  Result = i + b

During processing of the input, we can infer b, so it's a matter of solving the
above equations for i.
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
        "https://adventofcode.com/2023/day/18/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)


goes = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}


def tadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def tmul(s, b):
    return tuple(s * y for y in b)


data = [parse('{} {:d} (#{})', d).fixed for d in data]

dirs = 'RDLU'
curr = (0, 0)
points = [curr]
boundary = 0
for d in data:
    dir = dirs[int(d[2][5:])]
    i = int(d[2][:5], 16)
    curr = tadd(curr, tmul(i, goes[dir]))
    points.append(curr)
    boundary += i

x = [d[0] for d in points]
y = [d[1] for d in points]

A = abs(sum((y[i] + y[i + 1]) * (x[i] - x[i + 1]) for i in range(len(x)-1)) // 2)
b = boundary
i = A - b // 2 + 1
print(i + b)
