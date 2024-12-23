'''
I way overcomplicated part 2 initially and solved it for the longest substring
of any length, rather than just length 4.
'''

from requests_cache import CachedSession
from collections import defaultdict, Counter
from heapq import heappop, heappush
from functools import cache
from itertools import product

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/22/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

def step_secret(secret):
    secret ^= secret * 64
    secret %= 16777216
    secret ^= secret // 32
    secret ^= secret * 2048
    secret %= 16777216
    return secret

def calculate_secret(secret, steps):
    for _ in range(steps):
        secret = step_secret(secret)
    return secret

def build_values(secret):
    steps = 2000
    result = [secret % 10]
    for _ in range(steps):
        secret = step_secret(secret)
        result.append(secret % 10)
    
    diffs = tuple(b - a for a, b in zip(result, result[1:]))
    
    return result, diffs

def get_score():
    results = defaultdict(int)
    for values, diffs in things:
        seen = set()
        for i in range(len(diffs) - 4):
            substring = diffs[i:i+4]
            if substring in seen:
                continue
            seen.add(substring)
            results[substring] += values[i + 4]
    return max(results.values())

data = [int(d) for d in data.splitlines()]

print(sum(calculate_secret(d, 2000) for d in data))
things = [build_values(d) for d in data]

print(get_score())