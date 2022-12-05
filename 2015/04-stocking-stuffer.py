from collections import namedtuple
from time import sleep
from requests_cache import CachedSession
from parse import parse

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/4/input', cookies=cookies)
    .content
    .strip()
)

from hashlib import md5

suffix = 0
while True:
    suffix += 1
    hash = md5(data + str(suffix).encode()).digest().hex()

    if hash.startswith('000000'):
        break

print(suffix)