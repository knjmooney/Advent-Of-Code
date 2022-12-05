from collections import namedtuple
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
    .get('https://adventofcode.com/2015/day/8/input', cookies=cookies)
    .content
    .decode()
    .splitlines()
)

# data = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']

print(
    sum(len(d) for d in data)
    - sum(len(eval(d)) for d in data),
    sum(len(d) + 2 + d.count('"') + d.count('\\') for d in data)
    - sum(len(d) for d in data)
)
