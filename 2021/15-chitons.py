import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
from bisect import bisect_left, insort
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/15-input.txt').read().splitlines()
data = [[int(e) for e in d] for d in data]

H = len(data)
W = len(data[0])
assert W == H

for row in data:
    for j in range(1, 5):
        row += [((d + j - 1) % 9) + 1 for d in row[:W]]

for i in range(1, 5):
    data += [[((d + i - 1) % 9) + 1 for d in row] for row in data[:H]]

H = len(data)
W = len(data[0])
assert W == H

def gnns(a, b):
    return [
        (i, j)
        for (i, j) in [(a + 1, b), (a, b + 1), (a - 1, b), (a, b - 1)]
        if (i, j) != (a, b) and 0 <= i < H and 0 <= j < W
    ]

class node:
    pass

seen_and_unvisited = [(0, 0, 0)]
unvisited = set((i, j) for i in range(H) for j in range(W))
node_score = {(0, 0): 0}
while unvisited:
    curr, i, j = seen_and_unvisited.pop(0)

    unvisited.remove((i, j))
    for nn in gnns(i, j):
        nn_score = node_score.get(nn)
        new_nn_score = min(nn_score, curr + data[nn[0]][nn[1]]) if nn_score else curr + data[nn[0]][nn[1]]
        node_score[nn] = new_nn_score
        if nn in unvisited:
            if nn_score:
                seen_and_unvisited.pop(bisect_left(seen_and_unvisited, (nn_score, nn[0], nn[1])))
            insort(seen_and_unvisited, (new_nn_score, nn[0], nn[1]))

print(node_score[(W-1, W-1)])
