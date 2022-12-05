"""
I overcomplicated it a bit. There are 2**n possible subsets, so you can enumerte all of them.
"""

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
    .get('https://adventofcode.com/2015/day/17/input', cookies=cookies)
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [int(d) for d in data]

buckets = [set()]
for i in range(1, 150 + 1):
    buckets.append(set())
    for j, d in enumerate(data):
        if i - d == 0:
            buckets[i].add(frozenset([j]))
        if i - d > 0:
            for lower in buckets[i - d]:
                if j not in lower:
                    buckets[i].add(frozenset([j, *lower]))


print('p1 =', len(buckets[-1]))

end = buckets[-1]
smallest_n = min(len(d) for d in end)
print('p2 =', sum(1 for d in end if len(d) == smallest_n))
