'''
Pure brute force. Takes ~8 seconds on M1
'''

from requests_cache import CachedSession
from collections import defaultdict
from itertools import product, chain

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/7/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = [d.split(':') for d in data]
data = [(int(d[0]), [int(e) for e in d[1].split()]) for d in data]

def check(data):
    target, numbers = data
    for c in product('+*|', repeat=len(numbers) - 1):
        result = numbers[0]
        for n, o in zip(numbers[1:], c):
            if o == '+':
                result += n
            elif o == '*':
                result *= n
            elif o == '|':
                result = int(str(result) + str(n))
        if result == target:
            return True
    return False

print(sum(int(d[0]) for d in data if check(d)))