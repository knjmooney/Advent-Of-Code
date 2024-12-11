'''
1D game of life. It looked like a dynamic programming problem, so I went
straight for functools.cache.
'''

from requests_cache import CachedSession
from collections import defaultdict
from functools import cache

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/11/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)
blinks = 75

@cache
def count(e, blinks):
    if blinks == 0:
        return 1

    f = str(e)
    if e == 0:
        return count(1, blinks - 1)
    elif len(f) % 2 == 0:
        return (
            count(int(f[:len(f)//2]), blinks - 1) + 
            count(int(f[len(f)//2:]), blinks - 1)
        )
    else:
        return count(e * 2024, blinks - 1)

print(sum(count(int(e), blinks) for e in data.split())) 
