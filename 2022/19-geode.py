"""
Slow, but it gets there. I needed to get a hint to check I was on the right 
track. The most important part was coming up with clever ways of pruning, which
were specific to the problem domain.
"""

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
import functools

dirname = os.path.dirname(__file__)
data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/19/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

data = [
    parse(
        'Blueprint {:d}: '
        'Each ore robot costs {:d} ore. '
        'Each clay robot costs {:d} ore. '
        'Each obsidian robot costs {:d} ore and {:d} clay. ' 
        'Each geode robot costs {:d} ore and {:d} obsidian.', d).fixed 
    for d in data
]

def get_costs(bp):
    return (
        (bp[1], 0    , 0    ),
        (bp[2], 0    , 0    ),
        (bp[3], bp[4], 0    ),
        (bp[5], 0    , bp[6])
    )

def element_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def element_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

@functools.cache
def gen_robots(bp, raw):
    result = [((0, 0, 0), raw)]
    for robot_id, robot_bp in enumerate(bp):
        new_raw = element_sub(raw, robot_bp)
        if not all(e >= 0 for e in new_raw):
            continue

        this_robot_count = tuple(int(id == robot_id) for id in range(len(bp)))
        result.append((this_robot_count, new_raw))
    return result

def can_make_geo(bp, raw):
    geo_bp = bp[3]
    return all(r >= g for g, r in zip(geo_bp, raw))

target = 32
def simulate(bp):
    seen_count = 0
    iterations = 0
    skipped = 0
    max_geo = 0
    benchmark = 25
    seen = set()
    queue = deque([(0, (1, 0, 0), (0, 0, 0), 0)])
    max_bps = [max(b) for b in zip(*bp)]
    while queue:
        iterations += 1
        time, robots, raw, geos = queue.popleft()

        if (robots, raw) in seen:
            seen_count += 1
            continue

        if time == benchmark:
            print('At timestep', benchmark)
            benchmark += 1

        if time == target:
            max_geo = max(max_geo, geos)
            continue

        if any(r > max_bp for r, max_bp in zip(robots, max_bps)):
            skipped += 1
            continue

        if can_make_geo(bp, raw):
            geos += target - time - 1
            raw = element_add(robots, raw)
            queue.append((time + 1, robots, element_sub(raw, bp[3]), geos))
            continue

        seen.add((robots, raw))

        for add_robots, add_raw in gen_robots(bp, raw):
            new_raw = element_add(robots, add_raw)
            new_robots = element_add(robots, add_robots)
            
            queue.append((time + 1, new_robots, new_raw, geos))

    print(iterations, seen_count, skipped)
    return max_geo

data = [get_costs(bp) for bp in data]
for i, bp in enumerate(data[:3], 1):
    print('Starting ', i)
    result = simulate(bp)
    print('Result =', result)
