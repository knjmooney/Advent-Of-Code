"""
Very slow solution
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict, deque
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/11/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

serial = int(data)

grid = {}
for y in range(1, 1 + 300):
    for x in range(1, 1 + 300):
        rackId = x + 10
        grid[(x, y)] = rackId * y 
        grid[(x, y)] += serial
        grid[(x, y)] *= rackId
        grid[(x, y)] //= 100
        grid[(x, y)] %= 10
        grid[(x, y)] -= 5

result = {}
for x in range(1, 301):
    print(x)
    for y in range(1, 301):
        result[(x, y, 0)] = 0
        for size in range(1, 301):
            if x + size > 300 or y + size > 300:
                break
            result[(x, y, size)] = result[(x, y, size - 1)]
            result[(x, y, size)] += grid[(x + size - 1, y + size - 1)]
            result[(x, y, size)] += sum(grid[(x + size - 1, i)] for i in range(y, y + size - 1))
            result[(x, y, size)] += sum(grid[(i, y + size - 1)] for i in range(x, x + size - 1))

print(max(result.items(), key=lambda x: x[1]))
