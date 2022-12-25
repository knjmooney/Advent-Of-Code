'''
The SNAFU encoder works, but I'm not quite sure how. Oh well, time to enjoy Christmas.
'''

from collections import Counter, defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain, cycle
import json
import math
import os
from pprint import pprint
import re
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
    .get('https://adventofcode.com/2022/day/25/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
)

def decode(d):
    result = 0
    for i, c in enumerate(reversed(d)):
        result += {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[c] * 5**i
    return result

def encode(d):
    s = ''
    rmap = {v : k for k, v in {'2': 2, '1': 1, '0': 0, '-': 4, '=': 3}.items()}
    carry = 0
    while d or carry:
        c = (d % 5) + carry
        carry = int(c == 3 or c == 4)
        s = rmap[c % 5] + s
        d //= 5
    return s

data = data.splitlines()
result = 0
for d in data:
     result += decode(d)
print(result, encode(result))