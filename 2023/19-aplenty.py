"""
Any > or < causes the algorithm to branch. We keep track of what range take each branch.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter, defaultdict
from itertools import (
    combinations_with_replacement,
    cycle,
    chain,
    repeat,
    islice,
    combinations,
    count,
)
from math import lcm, prod
import functools
import sys
from heapq import heappop, heappush


data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/19/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

rules, parts = data.split("\n\n")
rules = {
    e[0]: e[1] for rule in rules.splitlines() if (e := parse("{}{{{}}}", rule).fixed)
}
parts = [
    parse("{{x={:d},m={:d},a={:d},s={:d}}}", part).fixed for part in parts.splitlines()
]


def handleSplit(xs, split):
    start, length = xs
    if start < split and start + length > split:
        return (start, split - start), (split, start + length - split)
    elif start < split:
        return (start, length), (-1, 0)
    else:
        return (-1, 0), (start, length)


def doWorkflow(part, ruleId):
    if ruleId == "A":
        return [part]
    if ruleId == "R":
        return []
    result = []
    for bit in rules[ruleId].split(","):
        if ":" not in bit:
            return result + doWorkflow(part, bit)
        l, r = bit.split(":")
        if "<" in l:
            id, split = l.split("<")
            go, keep = handleSplit(part[id], int(split))
        else:
            id, split = l.split(">")
            keep, go = handleSplit(part[id], int(split) + 1)

        part = {**part, id: keep}
        rest = {**part, id: go}
        result += doWorkflow(rest, r)


part = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
result = doWorkflow(part, "in")
print(sum(prod(l for _, l in r.values()) for r in result))
