'''
Fun with list comprehensions
'''

import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/2/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

def safe(d):
    return (
        all(b - a in range(1, 4) for a, b in zip(d, d[1:]))
     or all(a - b in range(1, 4) for a, b in zip(d, d[1:]))
    )

data = [[int(d) for d in e.split()] for e in data]

print(sum(any(safe(d[:i] + d[i+1:]) for i in range(len(d))) for d in data))
