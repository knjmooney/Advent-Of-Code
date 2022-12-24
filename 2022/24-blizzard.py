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
    .get('https://adventofcode.com/2022/day/24/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
)

# data = '''#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#'''

# data = '''#.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#'''

def print_board(board):
    for i in range(-1, H + 1):
        for j in range(-1, W + 1):
            if i == -1 or i == H or j == -1 or j == W:
                print('#', end='')
            elif (i, j) not in board:
                print('.', end='')
            else:
                l = board[(i, j)]
                print(l[0] if len(l) == 1 else len(l), end='')
        print('')

def next_position(p, c):
    d = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }[c]
    return ((p[0] + d[0]) % H, (p[1] + d[1]) % W)


@functools.cache
def get_board(i):
    if i == 0:
        return orig_board
    board = get_board(i-1)
    result = defaultdict(list)
    for p, l in board.items():
        for c in l:
            np = next_position(p, c)
            # print(p, np, c)
            result[next_position(p, c)].append(c)     
    return result

def md(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def nns(a):
    return ((a[0] + d[0], a[1] + d[1]) for d in [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)])

data = data.splitlines()
H = len(data) - 2
W = len(data[0]) - 2
orig_board = {(i-1, j-1): [c] for i, r in enumerate(data) for j, c in enumerate(r) if c in ['>', '<', '^', 'v']}

start = (-1, 0)
end = (H-1, W-1)
queue = [(md(start, end), 0, start)]
seen = set()

while True:
    _, t, p = heappop(queue)
    if (t, p) in seen:
        continue
    seen.add((t, p))
    board = get_board(t + 1)
    if p == end:
        print('end', t + 1)
        break
    for nn in nns(p):
        if (not nn == start) and nn[0] <= -1 or nn[1] <= -1 or nn[0] >= H or nn[1] >= W:
            continue
        elif nn in board:
            continue
        heappush(queue, (t + md(nn, end), t + 1, nn))