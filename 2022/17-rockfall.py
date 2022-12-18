"""
Lots of off by 1 errors :eye_roll:

Each state is defined by

    (index of input, which shape, tuple of each accesible row)

I then cached the time and height at each state, and I waited until I had a 
cached state that fit in 'nicely'.

    if (target - old_t) % delta_t == 0: 
        print(old_h + ((target - old_t) // delta_t) * delta_h)

Not sure why, but my target time had to be -1.
"""

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


dirname = os.path.dirname(__file__)
data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/17/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
    .strip()
)

shapes = [
    "####",
    ".#.\n"
    "###\n"
    ".#.",
    "..#\n"
    "..#\n"
    "###",
    "#\n"
    "#\n"
    "#\n"
    "#",
    "##\n"
    "##"
]

shapes = [
    [
        (i, j) for i, row in enumerate(reversed(shape.splitlines())) 
        for j, e in enumerate(row) if e == '#'
    ]
    for shape in shapes
]

def get_blown(p, shape, blow):
    q = (p[0], p[1] + 1) if blow == '>' else (p[0], p[1] - 1)
    for rel_p in shape:
        piece = (q[0] + rel_p[0], q[1] + rel_p[1])
        if board[piece[0]] & (1 << piece[1]):
            return p
    return q

def fall(p, shape):
    q = (p[0] - 1, p[1])
    for rel_p in shape:
        piece = (q[0] + rel_p[0], q[1] + rel_p[1])
        if board[piece[0]] & (1 << piece[1]):
            return True, p
    return False, q

def gen_board_state(board, height):
    state = 0       
    for line in board[height::-1]:
        yield line
        state |= line 
        if state == 2**9 - 1:
            break

data = cycle(enumerate(data))
shapes = cycle(enumerate(shapes))
height = 0
heights = {}

time = 3000 # Just enough to find a repeating pattern
target = 1_000_000_000_000 - 1 # For some reason it's 1 less :shrug:

board = [2**9 - 1] + [2**8 + 1 for c in range(9) for _ in range(3 * (time + 2))]

for t in range(time):
    shape_id, shape = next(shapes)
    p = (height + 4, 3)
    hits = False
    while not hits:
        blow_id, blow = next(data)
        p = get_blown(p, shape, blow)
        hits, p = fall(p, shape)
        if hits:
            for rel_p in shape:
                piece = (p[0] + rel_p[0], p[1] + rel_p[1])
                board[piece[0]] |= (1 << piece[1])
            height = max(height, max(p[0] + i for i, _ in shape))
            state = (shape_id, blow_id, tuple(e for e in gen_board_state(board, height)))
            if state in heights:
                old_t, old_h = heights[state]
                delta_t = t - old_t
                delta_h = height - old_h
                if (target - old_t) % delta_t == 0: 
                    print(old_h + ((target - old_t) // delta_t) * delta_h)
                    exit(0)
            heights[state] = (t, height)
