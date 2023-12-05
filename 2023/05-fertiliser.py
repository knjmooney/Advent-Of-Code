"""
Part 2 was tricky, trying to figure out how to map ranges.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/5/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)


data = data.split('\n\n')

source = [int(e) for e in data[0].split(': ')[1].split()]
source = [(a, b) for a, b in zip(source[::2], source[1::2])]
maps = [[[int(x) for x in e.split()] for e in d.splitlines()[1:]] for d in data[1:]]

maps = [sorted(m, key=lambda x: x[1]) for m in maps]

def doMap(map, elem):
    result = []
    for row in map:
        dst, src, N = row 
        start, M = elem
        if M <= 0:
            break
        if src <= start:
            overlap = min(src + N - start, M)
            if overlap > 0:
                result.append((dst + (start - src), overlap))
                remaining = M - overlap
                elem = (src + N, remaining)
        elif src <= start + M:
            result.append((start, src - start))
            overlap = min(N, start + M - src)
            result.append((dst, overlap))
            remaining = start + M - src - overlap
            elem = (src + N, remaining)

    if elem[1] > 0:
        # Unmapped
        result.append(elem)

    return result

for map in maps:
    newSource = []
    for elem in source:
        newSource.extend(doMap(map, elem))
    source = newSource

print(sorted(source)[0][0])