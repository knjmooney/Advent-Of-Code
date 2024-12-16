'''
Walk around once to find the shortest distance, then walk around again to find
all paths of that distance. It's pretty slow, ~15 seconds on an M3. Could
probably be sped up by pruning the domain more.
'''

from requests_cache import CachedSession
from collections import defaultdict
from heapq import heappop, heappush

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/16/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = {(i, j): e for i, r in enumerate(data.splitlines()) for j, e in enumerate(r)}

def tadd(a, b):
    return a[0] + b[0], a[1] + b[1]

def walk():
    start = list(data.keys())[list(data.values()).index('S')]
    visited = set()
    toVisit = [(0, (start,), (0, 1))]

    while toVisit:
        score, path, d = heappop(toVisit)

        p = path[-1]

        if data[p] == 'E':
            return score

        if (p, d) in visited or data[p] == '#':
            continue

        visited.add((p, d))

        heappush(toVisit, (score + 1, path + (tadd(p, d),), d))
        heappush(toVisit, (score + 1000, path, (d[1], -d[0])))
        heappush(toVisit, (score + 1000, path, (-d[1], d[0])))

def walk_again(target):
    start = list(data.keys())[list(data.values()).index('S')]
    visited = {}
    toVisit = [(0, (start,), (0, 1))]
    result = set()

    while toVisit:
        score, path, d = heappop(toVisit)

        p = path[-1]

        if score > target:
            return result

        if data[p] == 'E':
            assert score == target
            result |= set(path)

        if data[p] == '#':
            continue

        if (p, d) in visited and visited[(p, d)] != score:
            continue

        visited[(p, d)] = score

        heappush(toVisit, (score + 1,    path + (tadd(p, d),), d))
        heappush(toVisit, (score + 1000, path                , (d[1], -d[0])))
        heappush(toVisit, (score + 1000, path                , (-d[1], d[0])))

result = walk()
print(result)
result = walk_again(result)
print(len(result))