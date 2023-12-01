import json
from requests_cache import CachedSession
from collections import Counter

data = (
    CachedSession()
    .get('https://adventofcode.com/2018/day/2/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

# data = [Counter(d) for d in data]
# data = [(2 in d.values(), 3 in d.values()) for d in data]
# print(sum(d[0] for d in data) * sum(d[1] for d in data))

def differsByOne(a, b):
    assert len(a) == len(b)
    return sum(i != j for i, j in zip(a, b)) == 1

for a in data:
    for b in data:
        if differsByOne(a, b):
            print(''.join(i for i, j in zip(a, b) if i == j))