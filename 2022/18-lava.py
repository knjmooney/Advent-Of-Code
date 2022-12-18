from collections import Counter, defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain, cycle
import json
import os
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod
from heapq import heappop, heappush


dirname = os.path.dirname(__file__)
data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/18/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

def nns(p):
    return [
        (p[0] + 1, p[1], p[2]),
        (p[0] - 1, p[1], p[2]),
        (p[0], p[1] + 1, p[2]),
        (p[0], p[1] - 1, p[2]),
        (p[0], p[1], p[2] + 1),
        (p[0], p[1], p[2] - 1),        
    ]

# data='''2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5'''.splitlines()


data = [parse('{:d},{:d},{:d}', d).fixed for d in data]
minz = min(z for x, y, z in data)
maxz = max(z for x, y, z in data)
miny = min(y for x, y, z in data)
maxy = max(y for x, y, z in data)
minx = min(x for x, y, z in data)
maxx = max(x for x, y, z in data)
minp = (minx, miny, minz)
maxp = (maxx, maxy, maxz)

def surface_area(data):
    sa = 0
    for p in data:
        for nn in nns(p):
            sa += (nn not in data)
    return sa

def in_box(p):
    return (
        minp[0] <= p[0] <= maxp[0] and
        minp[1] <= p[1] <= maxp[1] and
        minp[2] <= p[2] <= maxp[2]
    )

seen = set()
def walk(p):
    hit_wall = False
    to_check = [p]
    shape = tuple()
    while to_check:
        p = to_check.pop()
        shape += (p,)
        seen.add(p)
        for nn in nns(p):
            if not in_box(nn):
                hit_wall = True
            elif nn not in to_check and nn not in seen and nn not in data:
                to_check.append(nn)
    return hit_wall, shape

air_sa = 0
for z in range(minz, 1 + maxz):
    for y in range(miny, 1 + maxy):
        for x in range(minx, 1 + maxx):
            p = (x, y, z)
            if p not in data and p not in seen:
                hit_wall, shape = walk((x, y, z))
                if not hit_wall:
                    air_sa += surface_area(shape)

print(surface_area(data))
print(surface_area(data) - air_sa)
