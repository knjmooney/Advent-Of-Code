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
    .get('https://adventofcode.com/2015/day/9/input', cookies=cookies)
    .content
    .decode()
    .splitlines()
)

data = [parse('{fm} to {to} = {v:d}', d).named for d in data]
locs = {*(d['fm'] for d in data), *(d['to'] for d in data)}

values = {}
for d in data:
    fm, to, v = d.values()
    values[(fm, to)] = v
    values[(to, fm)] = v

scores = [sum(values[(p, q)] for p, q in zip(perm, perm[1:])) for perm in permutations(locs)]
print(min(scores))
print(max(scores))
