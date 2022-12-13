'''
I initially thought S and E were 1 lower/higher than the rest of the board, 
but this was wrong. I guessed the correct answer, fortunately I was only off
by 2. When I got to part 2, the constraint didn't make sense, so when I went
back and saw S == a and E == z, it all dawned on me.
'''

from collections import defaultdict, deque, namedtuple
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
    .get('https://adventofcode.com/2022/day/12/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

N = len(data[0])
board = {}
for i, r in enumerate(data):
    for j, e in enumerate(r):
        board[(i, j)] = e
        if e == 'S':
            S = (i, j)
        if e == 'E':
            E = (i, j)

board[S] = 'a'
board[E] = 'z'
nns = [(0, 1), (0, -1), (1, 0), (-1, 0)]
As = [k for k, v in board.items() if v == 'a']
visited = set()

# Saw this clever optimisation on reddit
queue = [(0, a) for a in As]

while queue:
    score, current = heappop(queue)
    if current in visited:
        continue
    visited.add(current)
    if current == E:
        print(score)
        break
    for nn in nns:
        nextnn = (current[0] + nn[0], current[1] + nn[1])
        if (nextnn in board and ord(board[nextnn]) - ord(board[current]) <= 1):
            heappush(queue, (score + 1, nextnn))

