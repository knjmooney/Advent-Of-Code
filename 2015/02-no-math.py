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
    .get('https://adventofcode.com/2015/day/2/input', cookies=cookies)
    .content
    .decode("utf-8")
    .splitlines()
)

Parcel = namedtuple('Parcel', ['l', 'w', 'h'])
data = [Parcel(*parse("{:d}x{:d}x{:d}", d).fixed) for d in data]

data = [
    (
        (d.w * d.l, d.w * d.h, d.h * d.l),
        (2 * (d.w + d.l), 2 * (d.w + d.h), 2 * (d.h + d.l)),
        d.w * d.l * d.h
    )
    for d in data
]

data = [
    (
        min(d[0]),
        2 * d[0][0] + 2 * d[0][1] + 2 * d[0][2],
        min(d[1]),
        d[2]
    )
    for d in data
]

print('p1 =', sum(d[0] for d in data) + sum(d[1] for d in data))
print('p2 =', sum(d[2] for d in data) + sum(d[3] for d in data))
