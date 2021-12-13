import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = [[int(d) for d in line] for line in open(f'{dirname}/09-input.txt').read().splitlines()]
H = len(data)
W = len(data[0])

def nn(i, j):
    nns = [(y, x) for y, x in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
           if not (y == H or x == W or y == -1 or x == -1)]
    return nns

def explore(i, j, visited):
    visited.add((i, j))
    ret = [data[i][j]]
    for n in nn(i, j):
        if data[n[0]][n[1]] != 9 and n not in visited:
            ret += explore(n[0], n[1], visited)
    return ret

nns = [[nn(i, j) for j in range(W)] for i in range(H)]
low_point = [[all(data[x[0]][x[1]] > data[i][j] for x in nns[i][j]) for j in range(W)] for i in range(H)]
score = sum([data[i][j] + 1 for j in range(W) for i in range(H) if low_point[i][j]])
print(score)

print(prod(sorted([len(explore(i, j, set())) for j in range(W) for i in range(H) if low_point[i][j]])[-3:]))