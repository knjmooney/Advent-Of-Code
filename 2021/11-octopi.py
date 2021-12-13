import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/11-input.txt').read().splitlines()
messages = data.split('\n\n')[1].splitlines()
data = [[int(e) for e in d] for d in data]

L = len(data)
def gnns(a, b):
    return [
        (i, j)
        for i in (a-1, a+0, a+1)
        for j in (b-1, b+0, b+1)
        if (i, j) != (a, b) and 0 <= i < L and 0 <= j < L
    ]

flash = 0
def update(data):
    global flash
    data = [[v + 1 for v in r] for r in data]
    while any(v > 9 for r in data for v in r):
        for i in range(L):
            for j in range(L):
                if data[i][j] > 9:
                    flash += 1
                    data[i][j] = 0
                    for nn in gnns(i, j):
                        if data[nn[0]][nn[1]] != 0:
                            data[nn[0]][nn[1]] = data[nn[0]][nn[1]] + 1
    return data

for i in range(1000):
    if all(v == 0 for r in data for v in r):
        print(f'step {i}')
        break
    data = update(data)
print(messages)