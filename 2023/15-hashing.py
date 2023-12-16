"""
Someone pointed out this is a hash table.
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
from math import lcm
import functools

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/15/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = data.split(",")
boxes = defaultdict(list)


def getHash(d):
    result = 0
    for c in d:
        result += ord(c)
        result *= 17
        result %= 256
    return result


def insert(d):
    newLense = d.split('=')
    boxId = getHash(newLense[0])
    box = boxes[boxId]
    inserted = False
    for i in range(len(box)):
        if newLense[0] == box[i][0]:
            box[i] = newLense
            inserted = True
            break
    if not inserted:
        box.append(newLense)


def remove(d):
    removeId = d.strip('-')
    boxId = getHash(removeId)
    box = boxes[boxId]
    for i in range(len(box)):
        if removeId == box[i][0]:
            del box[i]
            return



for d in data:
    if "=" in d:
        insert(d)
    else:
        remove(d)


result = 0
for boxId, contents in boxes.items():
    for pos, (_, focal) in enumerate(contents, 1):
        result += (boxId + 1) * pos * int(focal)

print(result)
