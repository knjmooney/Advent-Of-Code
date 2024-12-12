'''
This one was fun. No particular trick. Use DFS to find the fields, and then find
all the edges one by one, being careful not to count an edge more than once.
'''

from requests_cache import CachedSession
from collections import defaultdict

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/12/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = {i + j * 1j: data[i][j] for i in range(len(data)) for j in range(len(data[0]))}

def walk(start):
    toVisit = {start}
    group = set()

    dir = -1
    while toVisit:
        p = toVisit.pop()
        group.add(p)
        for i in range(4):
            dir *= 1j
            nextp = p + dir
            if nextp not in group and data.get(nextp) == data[p]:
                toVisit.add(nextp)

    return group

def calc_perim(p):
    result = 0
    dir = 1
    for i in range(4):
        dir *= 1j
        nextp = p + dir
        result += data.get(nextp) != data[p]
    return result

def get_edge(start, dir):
    nextp = start + dir
    p = start
    v = data[p]
    result = set()
    while data.get(nextp) != v and data.get(p) == v:
        p += dir * 1j
        nextp = p + dir
        result.add((p, dir))

    nextp = start + dir
    p = start
    while data.get(nextp) != v and data.get(p) == v:
        p += dir * -1j
        nextp = p + dir
        result.add((p, dir))
    
    return result

def find_edges(group):
    checked = set()
    result = []
    while group:
        p = group.pop()

        dir = 1
        for i in range(4):
            dir *= 1j
            nextp = p + dir
            if data.get(nextp) != data[p] and (p, dir) not in checked:
                edge = get_edge(p, dir)
                checked |= edge
                result.append(edge)
    return result


remaining = set(data)
groups = []
while remaining:
    e = remaining.pop()
    group = walk(e)
    remaining -= group
    groups.append(group)

result = 0
for group in groups:
    area = len(group)
    perimeter = sum(calc_perim(e) for e in group)
    result += area * perimeter

print(result)

result = 0
for group in groups:
    area = len(group)
    perimeter = len(find_edges(group))
    result += area * perimeter

print(result)