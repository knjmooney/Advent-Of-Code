from collections import namedtuple
from distutils.errors import DistutilsClassError
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
    .get('https://adventofcode.com/2015/day/14/input', cookies=cookies)
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [
    parse('{name} can fly {speed:d} km/s for {mtime:d} seconds, but then must rest for {rtime:d} seconds.', d).named
    for d in data
]

def distance_travelled(d, total_time):
    name, speed, mtime, rtime = d.values()
    loops = total_time // (d['mtime'] + d['rtime'])
    remainder = total_time % (d['mtime'] + d['rtime'])
    final_move_time = min(remainder, mtime)
    total_move_time = mtime * loops + final_move_time
    return total_move_time * speed


print('p1 =', max(distance_travelled(d, 2503) for d in data))

points = {d['name']: 0 for d in data}

for i in range(1, 2504):
    max_dist = max(distance_travelled(d, i) for d in data)
    reindeers_in_lead = [d['name'] for d in data if distance_travelled(d, i) == max_dist]
    for r in reindeers_in_lead:
        points[r] += 1

print('p2 =', max(points.values()))
