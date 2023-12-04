"""
This was a tricky one, especially with no example for part 2.

My solution in the end involved discovering that it starts shifting by a fixed
delta once it has settled. I'm a little confused how I'm not off by 1. Oh well.
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict, deque
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/12/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

state = frozenset(e for e, v in enumerate(data[0].split(': ')[1]) if v =='#')
trans = {e[0] for d in data[2:] if (e := d.split(' => '))[1] == '#'}

def doTransform(state):
    start, end = min(state) - 4, max(state)
    newState = set()
    for i in range(start, end):
        key = ''.join('#' if j in state else '.' for j in range(i, i+5))
        if key in trans:
            newState.add(i + 2)
    return frozenset(newState)

seen = {state}
for i in range(200000):
    state = doTransform(state)
    normaliser = min(state)
    normalisedState = frozenset(e - normaliser for e in state)
    if normalisedState in seen:
        print('seen', normaliser)
        break
    seen.add(normalisedState)

oldState = state
delta = sum(doTransform(state)) - sum(oldState)
N = 50_000_000_000
print((N - i - 1) * delta + sum(state))
