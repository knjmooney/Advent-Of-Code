from collections import namedtuple
from distutils.errors import DistutilsClassError
from itertools import combinations, combinations_with_replacement, groupby, permutations, product
from time import sleep
from exceptiongroup import catch
from matplotlib.pyplot import text
from requests_cache import CachedSession
from parse import parse, findall
from pprint import pprint
import json
import re

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/16/input', cookies=cookies)
    .content
    .strip()
    .decode()
    .splitlines()
)

the_real_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

data = [
    {
        'id': p[0],
        **{r[0]: int(r[1]) for q in p[1].split(', ') if (r := q.split(': '))}
    }
    for d in data
    if (p := parse('Sue {:d}: {}', d).fixed)
]

def check(s, d):
    if s in ['cats', 'trees']:
        return d[s] > the_real_sue[s]
    if s in ['pomeranians', 'goldfish']:
        return d[s] < the_real_sue[s]
    return d[s] == the_real_sue[s]


for d in data:
    id = d['id']
    d = {k: v for k, v in d.items() if k != 'id'}
    if all(check(s, d) for s in d.keys()):
        print(id)
