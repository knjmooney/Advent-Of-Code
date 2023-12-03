"""
A challenging parsing problem. First identify symbols, then scan each adjacent
node for digits, uniquely identifying numbers by their start index.

A lot of opportunities for off by one errors, but fortunately they all
resulted in key errors, so easily identified.
"""

import json
from requests_cache import CachedSession
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/3/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)


def identifyNumber(i, j):
    if not data[i][j].isdigit():
        return None
    while j >= 0 and data[i][j].isdigit():
        j -= 1
    return (i, j + 1)


def findPartNumbers(i, j):
    numbers = set()
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            foundNumber = identifyNumber(k, l)
            if foundNumber:
                numbers.add(foundNumber)
    return numbers


def parseInt(i, j):
    k = j
    while k < len(data[i]) and data[i][k].isdigit():
        k += 1
    return int(data[i][j:k])


numbers = []
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == "*":
            partNumbers = findPartNumbers(i, j)
            if len(partNumbers) == 2:
                n = partNumbers.pop()
                m = partNumbers.pop()
                numbers.append(parseInt(n[0], n[1]) * parseInt(m[0], m[1]))


print(sum(n for n in numbers))
