import re
import os
from collections import Counter, namedtuple
from itertools import combinations, product
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod, sqrt
from bisect import bisect_left, insort
from copy import deepcopy
dirname = os.path.dirname(__file__)

def gnns(i, j):
    return [(a, b) for a in [i - 1, i, i + 1] for b in [j - 1, j, j + 1]]

def out_of_bounds(i, j):
    return not (imin <= i <= imax and jmin <= j <= jmax)

def next_state(i, j, image):
    lookup_id = ''
    for nn in gnns(i, j):
        lookup_id += '1' if image.get(nn, '.' if iteration % 2 == 0 else pixels[0]) == '#' else '0'
    return pixels[int(lookup_id, 2)]

pixels, image = open(f'{dirname}/20-test-input.txt').read().split('\n\n')
image = image.splitlines()
image = {(i, j): image[i][j] for i in range(len(image)) for j in range(len(image[0]))}

for iteration in range(50):
    imin = min(i for i, _ in image)
    jmin = min(j for _, j in image)
    imax = max(i for i, _ in image)
    jmax = max(j for _, j in image)
    image = {(i, j) : next_state(i, j, image) for i in range(imin - 2, imax + 3) for j in range(jmin - 2, jmax + 3)}

print(len([i for i in image.values() if i == '#']))
