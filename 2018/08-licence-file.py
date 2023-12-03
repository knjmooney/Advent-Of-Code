"""
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/8/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .split()
)

def parse(i, data):
    nChildNodes = data[i]
    nMetaData = data[1 + i]
    i += 2

    children = []
    for _ in range(nChildNodes):
        i, childScore = parse(i, data)
        children.append(childScore)

    metadata = []
    for _ in range(nMetaData):
        metadata.append(data[i])
        i += 1

    score = 0
    if len(children) == 0:
        score = sum(metadata)
    else:
        for ref in metadata:
            if ref <= len(children):
                score += children[ref - 1] 

    return (i, score)

data = [int(d) for d in data]

print(parse(0, data))
