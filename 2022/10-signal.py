from collections import deque, namedtuple
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/10/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

X = [1]
for d in data:
    if d == 'noop':
        X.append(X[-1])
    else:
        op, n = d.split(' ')
        assert op == 'addx'
        X.append(X[-1])
        X.append(X[-1] + int(n))

print(sum(X[s-1] * s for s in (20, 60, 100, 140, 180, 220)))

screen = ['.' for _ in range(40) for _ in range(6)]
for i, x in enumerate(X):
    if x - 1 <= i%40 <= x + 1:
        screen[i] = '#'

print(
    '\n'.join(''.join(screen[i:i+40]) 
    for i in range(0, 40 * 6, 40))
)
