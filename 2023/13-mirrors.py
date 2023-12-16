"""
Not the nicest of solutions. Someone pointed out you could rotate and just
compare whole rows at a time.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import (
    combinations_with_replacement,
    cycle,
    chain,
    repeat,
    islice,
    combinations,
)
from math import lcm
import functools

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/13/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = [[list(r) for r in d.splitlines()] for d in data.split("\n\n")]


def findReflection(m):
    next = list(range(1, len(m[0])))
    for r in m:
        prev = next
        next = []
        while prev:
            i = prev.pop()
            w = min(len(r) - i, i)
            if r[i - w : i] == r[i - 1 + w : i - 1 : -1]:
                next.append(i)
    return next


def toggle(e):
    return '#' if e == '.' else '.'


def score(m):
    old = set()
    old.update(findReflection(m))
    old.update(100 * e for e in findReflection(list(zip(*m))))
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = toggle(m[i][j])
            new = set()
            new.update(findReflection(m))
            new.update(100 * e for e in findReflection(list(zip(*m))))
            new -= old
            if new:
                assert len(new) == 1
                return next(iter(new))
            m[i][j] = toggle(m[i][j])



print(sum(score(m) for m in data))
