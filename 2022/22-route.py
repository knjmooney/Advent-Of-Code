'''
I modified part 1 to simplify as much as possible until one of the operations
was a string. At this point it was a matter of solving an algebraic equation,
it could have been done by hand, but I chose to write a basic solver instead.
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

# data = '''\
#         ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 10R5L5R10L4R5L5'''

R=0
D=1
L=2
U=3
facings = {(0, 1) : R, (1, 0): D, (0, -1) : L, (-1, 0): U,}


def read_tile_structure(board):
    # Not sure how to infer this
    n_tiles_high, n_tiles_wide = (4, 3) if W == 150 else (3, 4)
    tile_width = W // n_tiles_wide
    tile_height = H // n_tiles_high
    assert tile_height == tile_width
    
    result = []
    for i in range(0, H, tile_height):
        for j in range(0, W, tile_width):
            if board[(i, j)] != ' ':
                nns = [(i + x * tile_height, j + y * tile_width) for x, y in facings]
                neighbours = [
                    (i // tile_width, j // tile_width) 
                    if (i, j) in board and board[(i, j)] != ' ' 
                    else None for i, j in nns
                ]
                result.append(neighbours)
    return result

add = lambda a, b: ((a[0] + b[0]) % H, (a[1] + b[1]) % W)
def move(p, d, n):
    new_p = add(p, d)
    moved = 0
    while board[new_p] != '#' and moved < n:
        if board[new_p] == '.':
            p = new_p
            moved += 1
        # else:
            # assert board[new_p] == ' '

        new_p = add(new_p, d)
    return p, d


data = data.split('\n\n')
data[0] = data[0].splitlines()
W = max(len(d) for d in data[0])
H = len(data[0])
board = {(i, j): c for i, d in enumerate(data[0]) for j, c in enumerate(d + (' ' * (W - len(d))))}
ops = re.findall('L|R|\d+', data[1])

dir = (0, 1)
op : str
p = (0, min(i for i, c in enumerate(data[0][0]) if c != ' '))

for op in ops:
    if op.isalpha():
        dir = (-dir[1], dir[0]) if op == 'L' else (dir[1], -dir[0])
    else:
        assert op.isnumeric()
        p, dir = move(p, dir, int(op))        

facing = facings[dir]
print(p, facing)
print(1000 * (p[0] + 1) + 4 * (p[1] + 1) + facing)
print(read_tile_structure(board))
