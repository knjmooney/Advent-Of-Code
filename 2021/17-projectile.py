import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod, sqrt
from bisect import bisect_left, insort
data = 'target area: x=144..178, y=-100..-76'
# data = 'target area: x=20..30, y=-10..-5'
xl, xu, yl, yu = parse('target area: x={:d}..{:d}, y={:d}..{:d}', data)

def max_height(uy):
    return (uy * (uy + 1)) // 2


def does_it_hit(ux, uy):
    x, y = 0, 0
    vx, vy = ux, uy
    while x <= xu and y >= yl:
        x += vx
        y += vy
        vx = vx - 1 if vx != 0 else 0
        vy = vy - 1
        if xl <= x <= xu and yl <= y <= yu:
            return True


heights = []
for ux in range(1, xu + 1):
    for uy in range(yl - 1, abs(yl) + 1):
        if does_it_hit(ux, uy):
            heights.append(max_height(uy))

print(max(heights))
print(len(heights))
