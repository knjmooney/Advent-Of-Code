"""
I have a bug in my cycle detection which causes it to execute one more cycle
than it needs to. This is why I have a -2 in my remaining cycles calculation.
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
    count,
)
from math import lcm
import functools

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/14/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)


def getWeight(r):
    weight = 0
    N = len(r)
    for i, e in enumerate(r):
        if e == "O":
            weight += N - i
    return weight


def tilt(map):
    for r in map:
        obstruction = -1
        for i in range(len(r)):
            if r[i] == "O":
                obstruction += 1
                r[obstruction], r[i] = r[i], r[obstruction]
            elif r[i] == "#":
                obstruction = i
            else:
                assert r[i] == "."
    return map


def rotateLeft(map):
    map = [reversed(d) for d in map]
    return [list(d) for d in zip(*map)]


def rotate(map):
    return [list(reversed(d)) for d in zip(*map)]


def doCycle(map):
    for _ in range(4):
        map = tilt(map)
        map = rotate(map)
    return map


def doCycles(map):
    seen = set()
    for i in count():
        map = doCycle(map)
        cacheForm = "\n".join("".join(d) for d in rotate(map))
        if cacheForm in seen:
            print("seen", i)
            return (map, i)
        seen.add(cacheForm)


targetCycles = 1000000000

# The weight function and tilt function assume we start rotatedLeft.
data = rotateLeft(data)

data, i = doCycles(data)
data, j = doCycles(data)

# It cycles every j iterations, but we exhausted 1 + i cycles to step into the
# cycle, and then we exhausted j + 1 cycles to check the length of a cycle.
remainingCycles = (targetCycles - 2 - i - j) % j
print(remainingCycles)
for i in range(remainingCycles):
    data = doCycle(data)
print(sum(getWeight(d) for d in data))
