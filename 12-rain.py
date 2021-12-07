from collections import Counter, namedtuple
from itertools import combinations
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
# from math import abs
dirname = os.path.dirname(__file__)
Op = namedtuple('Op', ['cmd', 'arg'])
ops = [Op(s[0], int(s[1:])) for s in open(f'{dirname}/12-input.txt').read().splitlines()]

dir = ['E', 'S', 'W', 'N']
travel = [0, 0, 0, 0]
waypoint = [10, 0, 0, 1]
for op in ops:
    if op.cmd == 'F':
        travel[0] += waypoint[0] * op.arg
        travel[1] += waypoint[1] * op.arg
        travel[2] += waypoint[2] * op.arg
        travel[3] += waypoint[3] * op.arg
    elif op.cmd == 'L':
        turns = op.arg // 90
        waypoint = waypoint[turns:] + waypoint[:turns]
    elif op.cmd == 'R':
        turns = op.arg // 90
        waypoint = waypoint[-turns:] + waypoint[:-turns]
    elif op.cmd == 'E':
        waypoint[0] += op.arg
    elif op.cmd == 'S':
        waypoint[1] += op.arg
    elif op.cmd == 'W':
        waypoint[2] += op.arg
    elif op.cmd == 'N':
        waypoint[3] += op.arg

print(abs(travel[0] - travel[2]) + abs(travel[1] - travel[3]))
