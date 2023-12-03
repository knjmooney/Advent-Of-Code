"""
Kept iterating until I found the the minimum area.
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict, deque
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/10/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .replace(' ', '')
    .splitlines()
)

data = [list(parse('position=<{:d},{:d}>velocity=<{:d},{:d}>', d).fixed) for d in data]

areas = []
for iter in range(10605):
    for d in data:
        d[0] += d[2]
        d[1] += d[3]
    lw = min(d[0] for d in data)
    rw = max(d[0] for d in data)
    lh = min(d[1] for d in data)
    rh = max(d[1] for d in data)
    area = (rw - lw) * (rh - lh)
    areas.append((iter, area))

dots = {(d[0], d[1]) for d in data}
lw = min(d[0] for d in data)
rw = max(d[0] for d in data)
lh = min(d[1] for d in data)
rh = max(d[1] for d in data)

for i in range(lh, 1 + rh):
    for j in range(lw, 1 + rw):
        print('#' if (j, i) in dots else ' ', end='')
    print('')

pprint(min(areas, key=lambda x: x[1]))