from collections import defaultdict, deque, namedtuple
from functools import cmp_to_key
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod
from heapq import heappop, heappush

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/13/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .split('\n\n')
)

def check_pair(left, right):
    result = 0
    for l, r in zip(left, right):
        if isinstance(l, list) and isinstance(r, list):
            result = check_pair(l, r)
        elif isinstance(l, list):
            result = check_pair(l, [r])
        elif isinstance(r, list):
            result = check_pair([l], r)
        elif l < r:
            return -1
        elif l > r:
            return 1
        
        if result != 0:
            return result

    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
 
    assert result == 0
    return result

data.append('[[2]]\n[[6]]')
data = [eval(e) for d in data for e in d.splitlines()]
data = sorted(data, key=cmp_to_key(check_pair))
print((data.index([[2]]) + 1) * (data.index([[6]]) + 1))