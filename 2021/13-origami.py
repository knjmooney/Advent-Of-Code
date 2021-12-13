import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from typing import List
from graph import Graph
from parse import parse, findall
from math import prod
from dataclasses import dataclass
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/13-input.txt').read().split('\n\n')
dots = {(int(s[0]), int(s[1])) for d in data[0].splitlines() if (s := d.split(','))}
cmds = [parse('fold along {}={:d}', d).fixed for d in data[1].splitlines()]

def print_dots(dots):
    H = max(dots, key=lambda t: t[1])[1] + 1
    W = max(dots, key=lambda t: t[0])[0] + 1
    for i in range(H):
        for j in range(W):
            print('#' if (j, i) in dots else '.', end='')
        print('')


for cmd in cmds:
    if cmd[0] == 'y':
        dots = {(d[0], 2 * cmd[1] - d[1]) if d[1] >= cmd[1] else d for d in dots}
    else:
        dots = {(2 * cmd[1] - d[0], d[1]) if d[0] >= cmd[1] else d for d in dots}

    print('---- len =', len(dots))
print_dots(dots)

