from collections import namedtuple
from requests_cache import CachedSession
from parse import parse

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/3/input', cookies=cookies)
    .content
    .decode("utf-8")
)

p = (0, 0)
q = (0, 0)
visited = {p}
for d in data:
    p, q = q, p
    if d == '^':
        p = (p[0] + 1, p[1])
    elif d == '>':
        p = (p[0], p[1] + 1)
    elif d == '<':
        p = (p[0], p[1] - 1)
    elif d == 'v':
        p = (p[0] - 1, p[1])
    else:
        assert(False)
    visited.add(p)

print(len(visited))
