from collections import namedtuple
from itertools import combinations, permutations
from time import sleep
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
import re

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/10/input', cookies=cookies)
    .content
    .decode()
    .splitlines()
)

data = data[0]
for j in range(50):
    p = data[0]
    c = 0
    n = []
    for i, d in enumerate(data):
        if p == d:
            c += 1
        else:
            n.append(str(c))
            n.append(p)
            p = d
            c = 1
    n.append(str(c))
    n.append(p)
    data = n
print(len(n))
