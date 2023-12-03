"""
My initial solution worked but was quite slow, I would start from the beginning
after every reaction. I refactored it a little to restart from the previous
reaction site.
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/5/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

chars = [(chr(c), chr(c + 32)) for c in range(ord("A"), 1 + ord("Z"))]


def collapse(poly):
    i = 0
    while i + 1 < len(poly):
        j = i + 1
        if abs(ord(poly[i]) - ord(poly[j])) == 32:
            poly = poly[:i] + poly[j + 1 :]
            i = max(i - 1, 0)
        else:
            i += 1
    return poly


polyLen = len(data)
for char in chars:
    poly = data.replace(char[0], "").replace(char[1], "")
    poly = collapse(poly)
    polyLen = min(polyLen, len(poly))
print(polyLen)
