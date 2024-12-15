'''
###############################
#.............................#
#.............................#
#.............................#
#.............................#
#..............#..............#
#.............###.............#
#............#####............#
#...........#######...........#
#..........#########..........#
#............#####............#
#...........#######...........#
#..........#########..........#
#.........###########.........#
#........#############........#
#..........#########..........#
#.........###########.........#
#........#############........#
#.......###############.......#
#......#################......#
#........#############........#
#.......###############.......#
#......#################......#
#.....###################.....#
#....#####################....#
#.............###.............#
#.............###.............#
#.............###.............#
#.............................#
#.............................#
#.............................#
#.............................#
###############################
'''

from requests_cache import CachedSession
from collections import defaultdict, namedtuple
from parse import parse
from fractions import Fraction as frac

import json
import math
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/14/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)


Guard = namedtuple('Guard', ['px', 'py', 'vx', 'vy'])

guards = [
    Guard(*parse("p={:d},{:d} v={:d},{:d}", part).fixed) for part in data.splitlines()
]

niters = 100
w = 101
h = 103

def print_guards(guards):
    locs = {(g.px, g.py) for g in guards}
    for i in range(h):
        for j in range(w):
            print('#' if (j, i) in locs else '.', end='')
        print('')

def update_guards(guards):
    for i in range(len(guards)):
        g = guards[i]
        px = g.px + g.vx
        px %= w
        py = g.py + g.vy
        py %= h
        guards[i] = Guard(px, py, g.vx, g.vy)

print_guards(guards)

for iter in range(10000):
    update_guards(guards)
    if (iter + 4) % 101 == 0 and iter > 7000:
        print(f'\n{iter + 1}')
        print_guards(guards)

quads = [0, 0, 0, 0]
for g in guards:
    quads[0] += g.px < w // 2 and g.py < h // 2
    quads[1] += g.px < w // 2 and g.py > h // 2
    quads[2] += g.px > w // 2 and g.py < h // 2
    quads[3] += g.px > w // 2 and g.py > h // 2

print(math.prod(quads))