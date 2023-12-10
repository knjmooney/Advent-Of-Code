'''
Oddly straightforward for a Saturday.
'''

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import combinations_with_replacement, cycle, chain, repeat, islice
from math import lcm

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/9/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode().splitlines()
)

data = [[int(e) for e in d.split()] for d in data]

def nextValue(row):
    rows=[]
    while any(row):
        rows.append(row)
        row = [a - b for a, b in zip(row[1:], row)]
    while rows:
        prevRow = row
        row = rows.pop()
        row[-1] += prevRow[-1]
    return row[-1]

print(sum(nextValue(list(reversed(r))) for r in data))
