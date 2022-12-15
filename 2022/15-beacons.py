"""
The final solution ended up quite small, but it took me 150 minutes to get
there and the program runs in 30 seconds.

One nice solution I've seen is to only consider points that border the
diamonds, and check if each one falls inside another diamonds radius.
"""

from collections import defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain
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
    .get('https://adventofcode.com/2022/day/15/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .split('\n')
)

data = [parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', d).fixed for d in data]

ub = 4000000
board = [[] for _ in range(0, ub + 1)]
for sx, sy, bx, by in data:
    d = abs(by - sy) + abs(bx - sx)
    ylb = max(0, sy - d)
    yub = min(ub, sy + d)
    for ry in range(ylb, yub + 1):
        rx = d - abs(sy - ry)
        xlb = max(0, sx - rx)
        xub = min(ub, sx + rx)
        board[ry].append((xlb, xub))

for i, line in enumerate(board):
    line = sorted(line)
    max_so_far = line[0][1]
    for b in line[1:]:
        if b[0] > max_so_far + 1:
            print(4000000 * (max_so_far + 1) + i)
        max_so_far = max(b[1], max_so_far)
