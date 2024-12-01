'''
I initially assumed the righthand side was always bigger than the left.
'''

import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/1/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = [int(d) for d in data.split()]

l1 = sorted(data[::2])
l2 = sorted(data[1::2])

print(sum(abs(b - a) for a, b in zip(l1, l2)))
print(sum(a * l2.count(a) for a in l1))
