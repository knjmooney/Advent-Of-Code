'''
More complex numbers for coordinates. That way rotating 90 degrees is easy.

My end solution is quite slow, 20+ seconds on an M1. I could have been smarter
about only placing obstacles in the path.
'''

from requests_cache import CachedSession
from collections import defaultdict

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/6/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = {i + j * 1j: data[i][j] for i in range(len(data)) for j in range(len(data[0]))}

for d, v in data.items():
    if v == '^':
        pos = d
        break

def walk(pos, obs):
    if pos == obs:
        return False
    dir = -1
    visited = set()
    while pos in data:
        if (pos, dir) in visited:
            return True
        visited.add((pos, dir))
        nextp = pos + dir
        if data.get(nextp, '') == '#' or nextp == obs:
            dir *= -1j
        else:
            pos = nextp
    return False


print(sum(walk(pos, p) for p in data))