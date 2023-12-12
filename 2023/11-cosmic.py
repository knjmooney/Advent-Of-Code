"""
Part 1 is straightforward, tedious programming of the rules, and then you just
have to figure out what starting direction would work.

Part 2 is more interesting. We have the bounds from part 1, so we walk around
the loop and look either left or right, depending on whether the loop is
clockwise or anti-clockwise. I think I've hardcoded anti-clockwise.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import combinations_with_replacement, cycle, chain, repeat, islice, combinations
from math import lcm

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/11/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

# data = '''\
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....'''.splitlines()

planets = {(i, j) for i, r in enumerate(data) for j, e in enumerate(r) if e == '#'}
h = len(data)
w = len(data[0])

emptyRows = [not any((i, j) in planets for j in range(w)) for i in range(h)]
emptyCols = [not any((i, j) in planets for i in range(h)) for j in range(w)]

rowSum = [1000000 if emptyRows[i] else 1 for i in range(h)]
colSum = [1000000 if emptyCols[j] else 1 for j in range(w)]

rowSum = [sum(rowSum[:i]) for i in range(h)]
colSum = [sum(colSum[:j]) for j in range(w)]

def dist(p, q):
    a, b = p
    c, d = q
    return abs(rowSum[a] - rowSum[c]) + abs(colSum[b] - colSum[d])

print(sum(dist(p, q) for p, q in combinations(planets, 2)))

print(dist((2, 0), (6, 9)))