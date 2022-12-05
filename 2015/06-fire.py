from collections import namedtuple
from time import sleep
from requests_cache import CachedSession
from parse import parse
from pprint import pprint

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/6/input', cookies=cookies)
    .content
    .decode()
    .splitlines()
)
# print(parse('{} {:d},{:d} through {:d},{:d}', d).fixed)

data = [parse('{} {:d},{:d} through {:d},{:d}', d).fixed for d in data]
data = [
    {
        'ins': d[0],
        'start': (d[1], d[2]),
        'end': (d[3], d[4])
    }
    for d in data
]

grid = [[0 for i in range(1000)] for j in range(1000)]

for d in data:
    ins, start, end = d.values()
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if ins == 'turn on':
                grid[i][j] += 1
            elif ins == 'turn off':
                grid[i][j] = max(0, grid[i][j] - 1)
            elif ins == 'toggle':
                grid[i][j] += 2
            else:
                assert(False)

print(sum(d for r in grid for d in r))
