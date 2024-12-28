'''
'''

from requests_cache import CachedSession
from collections import defaultdict, Counter
from heapq import heappop, heappush

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/20/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

datas = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''

data = {(i, j): e for i, r in enumerate(data.splitlines()) for j, e in enumerate(r) if e != '#'}

def tadd(a, b):
    return a[0] + b[0], a[1] + b[1]

def walk():
    start = list(data.keys())[list(data.values()).index('E')]
    visited = {}
    toVisit = [(0, start)]

    while toVisit:
        score, p = heappop(toVisit)

        if p in visited:
            continue

        visited[p] = score

        if p in data and data[p] == 'S':
            return visited

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nextp = tadd(p, d)
            if nextp in data and nextp not in visited:
                heappush(toVisit, (score + 1, nextp))

def gend():
    result = []
    size = 20
    for i in range(size + 1):
        for j in range(size + 1 - i):
            result.append((+i, +j))
            result.append((-i, +j))
            result.append((+i, -j))
            result.append((-i, -j))
    return set(result)

scores = walk()
result = []
for p in scores:
    for d in gend():
        nextp = tadd(p, d)
        if nextp not in scores:
            continue
        saved = scores[nextp] - scores[p] - abs(d[0]) - abs(d[1])
        if saved >= 100:
            result += [(p, nextp, saved, scores[p], scores[nextp])]

# print(result)
print(len(result))
# print(Counter(r[2] for r in result))
# print([r for r in result if r[2] == 4])
