'''
I modified part 1 to simplify as much as possible until one of the operations
was a string. At this point it was a matter of solving an algebraic equation,
it could have been done by hand, but I chose to write a basic solver instead.
'''

from collections import Counter, defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain, cycle
import json
import os
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod
from heapq import heappop, heappush
import functools

dirname = os.path.dirname(__file__)
data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/21/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

@functools.cache
def get_monkey(monkey):
    if monkey == 'humn':
        return 'humn'

    v = data[monkey]
    if len(v) == 1:
        return int(*v)
    
    assert(len(v) == 3)
    m0, m1 = get_monkey(v[0]), get_monkey(v[2])

    if monkey == 'root':
        return [m0, '==', m1]

    if not (isinstance(m0, int) and isinstance(m1, int)):
        return [m0, v[1], m1]

    if v[1] == '+':
        return m0 + m1
    elif v[1] == '/':
        return m0 // m1
    elif v[1] == '*':
        return m0 * m1
    elif v[1] == '-':
        return m0 - m1

def solve(eq, result):
    if eq == 'humn':
        return f'humn == {result}'

    m0, op, m1 = eq
    if op == '/':
        result *= m1
        return solve(m0, result)
    elif op == '+' and isinstance(m1, int):
        result -= m1
        return solve(m0, result)
    elif op == '+' and isinstance(m0, int):
        result -= m0
        return solve(m1, result)
    elif op == '*' and isinstance(m1, int):
        result //= m1
        return solve(m0, result)
    elif op == '*' and isinstance(m0, int):
        result //= m0
        return solve(m1, result)
    elif op == '-' and isinstance(m1, int):
        result += m1
        return solve(m0, result)
    elif op == '-' and isinstance(m0, int):
        result = m0 - result
        return solve(m1, result)
    assert(False)

data = [parse('{}: {}', d).fixed for d in data]
data = {d[0]: d[1].split() for d in data}

result = get_monkey('root')
print(solve(result[0], result[2]))