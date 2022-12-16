"""
For part 1, I couldn't figure out an exit condition, so I kept printing the min
score, and just waited until it settled....

Since refactoring, I can check every possible state for part 1.

For part 2, I did A* with a heuristic based on time_left * factor. I kept 
tweaking the factor and rerunning until it found the answer....
Supposedly, I was most of the way there, the missing step was to introduce
memoization. So do DFS, but memoize the state somehow....
"""

from collections import defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain
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
    .get('https://adventofcode.com/2022/day/16/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
    .strip()
    .split('\n')
)

# data = '''\
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II'''.splitlines()

data = [d.split(';') for d in data]
data = [
    (
        list(parse('Valve {:S} has flow rate={:d}', d[0]).fixed) + 
        d[1].replace(',', '').split()[4:] 
    )
    for d in data
]

nodes = {origin: {'fr': fr, 'kids': children} for origin, fr, *children in data}

def costs(curr_node):
    visited = set()
    dists = {}
    queue = [(1, curr_node)]
    while len(visited) != len(nodes):
        score, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        fr = nodes[node]['fr']
        if fr and curr_node != node:
            dists[node] = (score)
        for kid in nodes[node]['kids']:
            heappush(queue, (score + 1, kid))

    return dists


for node in nodes:
    nodes[node]['costs'] = costs(node)

for node in nodes:
    nodes[node]['kids'] = nodes[node]['costs']
    del nodes[node]['costs']

nodes = {node: nodes[node] for node in nodes if nodes[node]['fr'] != 0 or node == 'AA'}

queue = [(0, 0, (-26, 'AA'), (-26, 'AA'), ())]
visited = set()

min_so_far = 0
while queue:
    state = heappop(queue)
    if state in visited:
        continue
    visited.add(state)

    h, score, p0, p1, open = state 

    assert (p0[0] <= 0 and p1[0] <= 0)
    if min_so_far > score:
        min_so_far = score
        print(min_so_far)

    assert p0 <= p1
    curr_time, curr_node = p0
    other = p1
    
    for kid, dist in nodes[curr_node]['kids'].items():
        if curr_time + dist > 0 or kid in open:
            continue
        fr = nodes[kid]['fr']
        new_score = score + fr * (curr_time + dist)
        new_open = tuple(sorted(open + (kid,)))
        next_p = (curr_time + dist, kid)
        p0, p1 = min(next_p, other), max(next_p, other)
        new_state = (new_score + p0[0]*79, new_score, p0, p1, new_open)
        heappush(queue, new_state)
