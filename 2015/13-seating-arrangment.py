from collections import namedtuple
from itertools import combinations, groupby, permutations
from time import sleep
from exceptiongroup import catch
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
    .get('https://adventofcode.com/2015/day/13/input', cookies=cookies)
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [
    parse('{fr} would {change} {value:d} happiness units by sitting next to {to}.', d).named
    for d in data
]

data = {
    k: {
        e['to']: e['value'] * (1 if e['change'] == 'gain' else -1)
        for e in v
    }
    for k, v in groupby(data, lambda x: x['fr'])
}

def get_score(p):
    return sum(data[a][b] + data[b][a] for a, b in zip(p, p[-1:] + p))


guests = list(data.keys())

print('p1 =', max(get_score(perm) for perm in permutations(guests)))

data['me'] = {}
for g in guests:
    data['me'][g] = 0
    data[g]['me'] = 0
guests += ['me']

print('p2 =', max(get_score(perm) for perm in permutations(guests)))

