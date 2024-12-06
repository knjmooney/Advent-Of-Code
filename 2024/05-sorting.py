'''
I implemeneted bubble sort rather than figuring out how to use built in sort.
'''

from requests_cache import CachedSession
from collections import defaultdict

import json
import re

data, lists = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/5/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .split('\n\n')
)

mappings = defaultdict(list)
for d in data.splitlines():
    k, v = d.split('|')
    mappings[k].append(v)

lists = [l.split(',') for l in lists.splitlines()]

def check(l):
    for i in range(len(l)):
        for j in range(i):
            if l[j] in mappings[l[i]]:
                return 0
    return int(l[len(l)//2])

def doSort(l):
    for i in reversed(range(len(l))):
        j = i - 1
        while j >= 0:
            if l[j] in mappings[l[i]]:
                l[j], l[i] = l[i], l[j]
                j = i - 1
            else:
                j -= 1
    return int(l[len(l)//2])



print(sum(check(l) for l in lists))
print(sum(doSort(l) for l in lists if check(l) == 0))
