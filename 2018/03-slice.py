import json
from requests_cache import CachedSession
from collections import Counter, defaultdict
from parse import parse

data = (
    CachedSession()
    .get('https://adventofcode.com/2018/day/3/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [parse("#{:d} @ {:d},{:d}: {:d}x{:d}", d).fixed for d in data]

patches = defaultdict(list)

for d in data:
    for i in range(d[1], d[1] + d[3]):
        for j in range(d[2], d[2] + d[4]):
            patches[(i, j)] += [d[0]]

max_overlaps = defaultdict(int)
for p in patches.values():
    for e in p:
        max_overlaps[e] = max(max_overlaps[e], len(p))

print([m for m, v in max_overlaps.items() if v == 1])