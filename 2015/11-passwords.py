"""It's a little slow, but I can't think of any clever optimisations"""

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
    .get('https://adventofcode.com/2015/day/11/input', cookies=cookies)
    .content
    .strip()
)

data = bytearray(data)

def straight_line(s):
    for s in zip(s, s[1:], s[2:]):
        if s[0] + 2 == s[1] + 1 == s[2]:
            return True
    return False

def is_pair(s):
    return s[0] == s[1]

def next_pair(s):
    for i, p in enumerate(zip(s, s[1:])):
        if p[0] == p[1]:
            return i
    return None

def non_overlapping_pairs(s):
    while (i := next_pair(s)) is not None:
        if next_pair(s[i + 2:]) is not None:
            return True
        s = s[i + 1:]
    return False

def meets_requirements(s):
    return straight_line(s) and not any(l in s for l in bytearray(b'iol')) and non_overlapping_pairs(s)

def increment(s: bytearray):
    s = s[::-1]
    i = 0
    while s[i] == ord('z'):
        s[i] = ord('a')
        i += 1
    s[i] = s[i] + 1
    return s[::-1]


while True:
    data = increment(data)
    if meets_requirements(data):
        break
print('p1 =', data)

while True:
    data = increment(data)
    if meets_requirements(data):
        break
print('p2 =', data)