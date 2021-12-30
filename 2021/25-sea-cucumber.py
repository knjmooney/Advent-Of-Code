from collections import Counter, deque
from pprint import pprint
import os
from parse import parse, findall
import re
from copy import deepcopy
dirname = os.path.dirname(__file__)


data = [list(d) for d in open(f'{dirname}/25-input.txt').read().splitlines()]

H = len(data)
W = len(data[0])

# def gnns(i, j):
#     return [
#         ((i - 1) % H, j),
#         ((i + 1) % H, j),
#         (i, (j - 1) % W),
#         (i, (j + 1) % W)
#     ]


def step(data):
    new_data = deepcopy(data)
    for i in range(H):
        for j in range(W):
            if data[i][(j - 1) % W] == '>' and data[i][j] == '.':
                new_data[i][j] = '>'
            elif data[i][j] == '>' and data[i][(j + 1) % W] == '.':
                new_data[i][j] = '.'

    data = deepcopy(new_data)
    for i in range(H):
        for j in range(W):
            if data[(i - 1) % H][j] == 'v' and data[i][j] == '.':
                new_data[i][j] = 'v'
            elif data[i][j] == 'v' and data[(i + 1) % H][j] == '.':
                new_data[i][j] = '.'
    return new_data

# pprint([''.join(d) for d in data])

old_data = None
count = 0
while old_data != data:
    old_data = data
    data = step(data)
    count += 1

print(count)
# pprint([''.join(d) for d in step(data)])
