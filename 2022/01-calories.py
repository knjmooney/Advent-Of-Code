import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/1/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
)

data = [[int(e) for e in d.splitlines()] for d in data.split('\n\n')]
sums = [sum(d) for d in data]
print(sum(sorted(sums)[-3:]))
