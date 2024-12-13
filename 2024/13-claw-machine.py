'''
'''

from requests_cache import CachedSession
from collections import defaultdict
from parse import parse
from fractions import Fraction as frac

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/13/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

parts = [
    parse("Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}", part).fixed for part in data.split('\n\n')
]

result=0
for part in parts:
    x0, y0, x1, y1, x, y = [frac(p) for p in part]
    x += 10000000000000
    y += 10000000000000
    x /= x0
    x1 /= x0
    x0 /= x0
    y -= y0 * x
    y1 -= y0 * x1
    y0 -= y0 * x0    
    y /= y1
    y1 /= y1
    x -= x1 * y
    x1 -= x1 * y1
    if x.is_integer() and y.is_integer():
        result += x * 3 + y * 1

print(result)