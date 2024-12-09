'''
Nothing special. I have separate objects to keep track of the map, common
antennas and antinode locations.
'''

from requests_cache import CachedSession
from collections import defaultdict
from itertools import product, chain, combinations

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/8/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

antennas = defaultdict(set)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '.':
            antennas[data[i][j]].add(i + j*1j)

board = {i + j * 1j: data[i][j] for i in range(len(data)) for j in range(len(data[0]))}

antinodes = set()
for antenna, locs in antennas.items():
    for a, b in combinations(locs, 2):
        newloc = a
        while newloc in board:
            antinodes.add(newloc)
            newloc += (b-a)        
        newloc = b
        while newloc in board:
            antinodes.add(newloc)        
            newloc += (a-b)        

print(len(antinodes))
