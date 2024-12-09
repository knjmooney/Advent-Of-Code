'''
I found part 2 tricky, especially figuring out the correct way to swap blocks
'''

from requests_cache import CachedSession
from collections import defaultdict
from itertools import product, chain, combinations, islice
from dataclasses import dataclass


import json
import re

def batched(iterable, n, *, strict=False):
    # Stolen from python 3.12
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/9/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

def part1(data):
    data = data + '0'

    fs = []
    id = 0
    for a, b in batched(data, 2):
        for i in range(int(a)):
            fs.append(str(id))
        for i in range(int(b)):
            fs.append('.')
        id += 1

    i = 0
    j = len(fs) - 1
    while i < j:
        if fs[i] != '.':
            i += 1
        elif fs[j] == '.':
            j -= 1
        else:
            fs[i], fs[j] = fs[j], fs[i]

    return sum(int(fs[j]) * j for j in range(i))

def compress(fs, j):
    i = 0
    b = fs[j]
    if b[0] == '.':
        return j - 1

    while i < j:
        a = fs[i]
        if a[0] != '.' or b[1] > a[1]:
            i += 1
            continue
        
        fs[i] = b
        fs[j] = (a[0], b[1])
        fs.insert(i + 1, ('.', a[1] - b[1]))
        return j
    
    return j - 1


def part2(data):

    data = data + '0'

    fs = []
    id = 0
    for a, b in batched(data, 2):
        fs.append((str(id), int(a)))
        fs.append(('.', int(b)))
        id += 1

    j = len(fs) - 1
    while j > 0:
        b = fs[j]
        j = compress(fs, j)

    factor = 0
    result = 0
    for id, count in fs:
        if id != '.':
            result += (count * factor + count * (count - 1) // 2) * int(id)
        factor += count

    return result

print(part1(data))
print(part2(data))
