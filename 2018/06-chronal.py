"""
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/6/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = {(int(e[1]), int(e[0])) : id for id, d in enumerate(data) if (e := d.split(', '))}

w = max(d[0] for d in data)
h = max(d[1] for d in data)
grid = defaultdict(list)
for d, id in data.items():
    for x in range(-1, 2 + w):
        for y in range(-1, 2 + h):
            grid[(x, y)].append((abs(d[0] - x) + abs(d[1] - y), id))

def getSite(p):
    closest, nextClosest = sorted(grid[p])[0:2]
    if closest[0] == nextClosest[0]:
        return '.'
    return chr(closest[1] + ord('A'))

infinities = set()
for x in range(-1, 2 + w):
    infinities.add(getSite((x, -1)))
    infinities.add(getSite((x, 1 + h)))

for y in range(-1, 2 + h):
    infinities.add(getSite((-1, y)))
    infinities.add(getSite((1 + w, y)))

areas = Counter(getSite(p) for p in grid)

valid = []
for id, area in areas.items():
    if id in infinities:
        continue
    valid.append(area)

print(sorted(valid)[-1])

def getSite2(p):
    return sum(d[0] for d in grid[p]) < 10000

print(sum(getSite2(p) for p in grid))