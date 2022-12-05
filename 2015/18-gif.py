from collections import namedtuple
from distutils.errors import DistutilsClassError
from itertools import combinations, combinations_with_replacement, groupby, permutations, product
from time import sleep
from exceptiongroup import catch
from matplotlib.pyplot import text
from requests_cache import CachedSession
from parse import parse, findall
from pprint import pprint
from heapq import merge
import json
import re

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/18/input', cookies=cookies)
    .content
    .strip()
    .decode()
    .splitlines()
)

data = {(i, j): v for i, d in enumerate(data) for j, v in enumerate(d)}

nns = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]

for _ in range(100):
    ndata = dict()
    for i in range(100):
        for j in range(100):
            count = sum(data.get((i + nn[0], j + nn[1])) == '#' for nn in nns)
            if data[(i, j)] == '#' and count in [2, 3]:
                ndata[(i, j)] = '#'
            elif data[(i, j)] == '.' and count == 3:
                ndata[(i, j)] = '#'
            else:
                ndata[(i, j)] = '.'
    ndata[(00, 00)] = '#'
    ndata[(99, 00)] = '#'
    ndata[(00, 99)] = '#'
    ndata[(99, 99)] = '#'
    data = ndata

print(sum(d == '#' for d in data.values()))
