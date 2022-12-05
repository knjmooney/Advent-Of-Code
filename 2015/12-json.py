"""It's a little slow, but I can't think of any clever optimisations"""

from collections import namedtuple
from itertools import combinations, permutations
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
    .get('https://adventofcode.com/2015/day/12/input', cookies=cookies)
    .content
    .strip()
    .decode()
)

def sum_of_children(data):
    if isinstance(data, str):
        return 0
    elif isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_of_children(e) for e in data)
    elif isinstance(data, dict):
        for v in data.values():
            if v == 'red':
                return 0
        return sum(sum_of_children(e) for e in data.values())
    else:
        assert False, f'{type(data)} not recognised'


print('p1 =', sum(e[0] for e in findall('{:d}', data)))

data = json.loads(data)
print(sum_of_children(data))