'''
Copied day 16. I did a semi manual search for part 2.
'''

from requests_cache import CachedSession
from collections import defaultdict
from heapq import heappop, heappush
from parse import parse

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/18/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

def tadd(a, b):
    return a[0] + b[0], a[1] + b[1]

def walk(steps):
    end = (70, 70)
    map = {(i, j) for i in range(end[0] + 1) for j in range(end[1] + 1)}

    for d in data.splitlines()[:steps]:
        e = parse("{:d},{:d}", d).fixed
        map.remove(e)

    start = (0, 0)
    visited = set()
    toVisit = [(0, start)]

    while toVisit:
        score, p = heappop(toVisit)

        if p == end:
            return score

        if p in visited or p not in map:
            continue

        visited.add(p)

        heappush(toVisit, (score + 1, (p[0] + 1, p[1])))
        heappush(toVisit, (score + 1, (p[0] - 1, p[1])))
        heappush(toVisit, (score + 1, (p[0], p[1] + 1)))
        heappush(toVisit, (score + 1, (p[0], p[1] - 1)))

for steps in range(2900, 5000):
    print(steps)
    result = walk(steps)
    if result is None:
        print(data.splitlines()[steps-1])
        exit()