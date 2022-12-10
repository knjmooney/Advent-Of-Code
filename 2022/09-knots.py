from collections import deque, namedtuple
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/9/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

knots = [(0, 0)] * 10
visited = {knots[-1]}

def move_head(head, dir):
    if dir == 'U':
        return (head[0] + 1, head[1])
    elif dir == 'D':
        return (head[0] - 1, head[1])
    elif dir == 'R':
        return (head[0], head[1] + 1)
    elif dir == 'L':
        return (head[0], head[1] - 1)    
    assert(False)

def move_knot(tail, head):
    if head[0] - tail[0] == 2:
        return (tail[0] + 1, tail[1] + np.sign(head[1] - tail[1]))
    elif head[0] - tail[0] == -2:
        return (tail[0] - 1, tail[1] + np.sign(head[1] - tail[1]))
    elif head[1] - tail[1] == 2:
        return (tail[0] + np.sign(head[0] - tail[0]), tail[1] + 1)
    elif head[1] - tail[1] == -2:
        return (tail[0] + np.sign(head[0] - tail[0]), tail[1] - 1)
    return tail

for d in data:
    dir, n, = d.split()
    n = int(n)
    for i in range(n):
        knots[0] = move_head(knots[0], dir)
        for i in range(len(knots) - 1):
            knots[i + 1] = move_knot(knots[i + 1], knots[i])
        visited.add(knots[-1])


print(len(visited))