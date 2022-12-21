from collections import Counter, defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain, cycle
import json
import os
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod
from heapq import heappop, heappush
import functools

dirname = os.path.dirname(__file__)
data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/20/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

data = [(i, 811589153 * int(d)) for i, d in enumerate(data)]

N = len(data)
result = data[:]
for _ in range(10):
    for i, d in data:
        old_i = result.index((i, d))
        new_i = (old_i + d) % (N - 1)
        result = (
            result[:old_i] + result[old_i+1:new_i+1] + [(i, d)] + result[new_i+1:]
            if new_i >= old_i else
            result[:new_i] + [(i, d)] + result[new_i:old_i] + result[old_i+1:]
        )

result = [r[1] for r in result]
i = result.index(0)
print(result[(i + 1000)%N] + result[(i + 2000)%N] + result[(i + 3000)%N])