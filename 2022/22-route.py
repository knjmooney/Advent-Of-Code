'''
This was a tricky one. I tried to make a generic solution, but in the end,
I hardcoded the shape.
'''

from collections import Counter, defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain, cycle
import json
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
    .get('https://adventofcode.com/2022/day/22/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
)

R=0
D=1
L=2
U=3
facings = {(0, 1) : R, (1, 0): D, (0, -1) : L, (-1, 0): U}
ifacings = {v: k for k, v in facings.items()}

N = 50
flip = lambda x: N - 1 - (x % N)
asis = lambda x: x % N
def boundary(p, d):
    new_p, new_d = {
        (0, 1): {
            U: ((3 * N + asis(p[1]), 0 * N), ifacings[R]),
            L: ((2 * N + flip(p[0]), 0 * N), ifacings[R])
        },
        (0, 2): {
            D: ((1 * N + asis(p[1]), 1 * N + asis(p[0])), ifacings[L]),
            R: ((2 * N + flip(p[0]), 1 * N + asis(p[1])), ifacings[L]),
            U: ((3 * N + flip(p[0]), 0 * N + asis(p[1])), ifacings[U])
        },
        (1, 1): {
            R: ((0 * N + asis(p[1]), 2 * N + asis(p[0])), ifacings[U]),
            L: ((2 * N + asis(p[1]), 0 * N + asis(p[0])), ifacings[D])
        },
        (2, 0): {
            L: ((0 * N + flip(p[0]), 1 * N), ifacings[R]),
            U: ((1 * N + asis(p[1]), 1 * N + asis(p[0])), ifacings[R])
        },
        (2, 1): {
            R: ((0 * N + flip(p[0]), 2 * N + asis(p[1])), ifacings[L]),
            D: ((3 * N + asis(p[1]), 0 * N + asis(p[0])), ifacings[L])
        },
        (3, 0): {
            L: ((0 * N, 1 * N + asis(p[0])), ifacings[D]),
            D: ((0 * N + flip(p[0]), 2 * N + asis(p[1])), ifacings[D]),
            R: ((2 * N + asis(p[1]), 1 * N + asis(p[0])), ifacings[U])
        }
    }[(p[0] // N, p[1] // N)][facings[d]]
    return new_p, new_d


add = lambda a, b: ((a[0] + b[0]), (a[1] + b[1]))
def move(p, d, n):
    new_p = p
    new_d = d
    moved = -1
    while board[new_p] != '#' and moved < n:
        assert board[new_p] == '.'
        p = new_p
        d = new_d
        moved += 1
        new_p = add(new_p, d)
        if new_p not in board or board[new_p] == ' ':
            new_p, new_d = boundary(p, d)
            assert board[new_p] != ' '

    return p, d


data = data.split('\n\n')
data[0] = data[0].splitlines()
W = max(len(d) for d in data[0])
H = len(data[0])
board = {(i, j): c for i, d in enumerate(data[0]) for j, c in enumerate(d + (' ' * (W - len(d))))}
ops = re.findall('L|R|\d+', data[1])

dir = (0, 1)
p = (0, min(i for i, c in enumerate(data[0][0]) if c != ' '))

op : str
for index, op in enumerate(ops):
    if op.isalpha():
        dir = (-dir[1], dir[0]) if op == 'L' else (dir[1], -dir[0])
    else:
        assert op.isnumeric()
        p, dir = move(p, dir, int(op))        

facing = facings[dir]
print(1000 * (p[0] + 1) + 4 * (p[1] + 1) + facing)
