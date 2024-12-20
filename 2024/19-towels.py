'''
Drunk dynamic programming :)
'''

from requests_cache import CachedSession
from collections import defaultdict
from heapq import heappop, heappush
from functools import cache

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/19/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

towels, targets = data.split('\n\n')

towels = towels.split(', ')
targets = targets.splitlines()

@cache
def is_valid(target:str):
    if target in towels:
        return 1 + sum(is_valid(target[len(towel):]) for towel in towels if target.startswith(towel))
    return sum(is_valid(target[len(towel):]) for towel in towels if target.startswith(towel))

print(sum(is_valid(d) for d in targets))
