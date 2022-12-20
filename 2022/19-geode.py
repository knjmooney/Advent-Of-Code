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

data = '''\
Blueprint 1: \
Each ore robot costs 4 ore. \
Each clay robot costs 2 ore. \
Each obsidian robot costs 3 ore and 14 clay. \
Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: \
Each ore robot costs 2 ore. \
Each clay robot costs 3 ore. \
Each obsidian robot costs 3 ore and 8 clay. \
Each geode robot costs 3 ore and 12 obsidian.'''.splitlines()

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
        (bp[1], 0    , 0    , 0),
        (bp[2], 0    , 0    , 0),
        (bp[3], bp[4], 0    , 0),
        (bp[5], 0    , bp[6], 0)
    )

def element_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])

def element_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])

@functools.cache
def gen_robots(bp, raw):
    result = [((0, 0, 0, 0), raw)]
    for robot_id, robot_bp in enumerate(bp):
        new_raw = element_sub(raw, robot_bp)
        if not all(e >= 0 for e in new_raw):
            continue
        
        this_robot_count = tuple(int(id == robot_id) for id in range(len(bp)))
        result.append((this_robot_count, new_raw))
    return result

def simulate(bp):
    seen_count = 0
    iterations = 0
    skipped = 0
    max_geo = 0
    seen = set()
    queue = deque([(0, (1, 0, 0, 0), (0, 0, 0, 0))])
    max_bps = [max(b) for b in zip(*bp)][:3]
    while queue:
        iterations += 1
        time, robots, raw = queue.popleft()

        if (robots, raw) in seen:
            seen_count += 1
            continue

        if time == 24:
            max_geo = max(max_geo, raw[3])
            continue

        if any(r > max_bp for r, max_bp in zip(robots, max_bps)):
            skipped += 1
            continue

        seen.add((robots, raw))

        for add_robots, add_raw in gen_robots(bp, raw):
            new_raw = element_add(robots, add_raw)
            new_robots = element_add(robots, add_robots)
            
            queue.append((time + 1, new_robots, new_raw))

    print(iterations, seen_count, skipped)
    return max_geo

data = [get_costs(bp) for bp in data]
for i, bp in enumerate(data, 1):
    print('Starting ', i)
    print('Result =', simulate(bp))
