'''
Required a little bit of reverse engineering of the input to develop a
backfilling algorithm.
'''

from requests_cache import CachedSession
from collections import defaultdict, Counter
from heapq import heappop, heappush
from functools import cache
from itertools import product
from parse import parse

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/17/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

a, b, c, ops = parse('''\
Register A: {:d}
Register B: {:d}
Register C: {:d}

Program: {}''', data).fixed

ops = [int(o) for o in ops.split(',')]

def compute(a):
    def combo(v):
        if v <= 3:
            return v
        if v == 4:
            return a
        if v == 5:
            return b
        if v == 6:
            return c
        assert False

    b = 0
    c = 0
    ip = 0
    result = []

    while True:
        if ip == len(ops):
            break
        
        op = ops[ip]
        vl = ops[ip + 1]

        if op == 0:
            a = a >> combo(vl)
        elif op == 1:
            b ^= vl
        elif op == 2:
            b = combo(vl) % 8
        elif op == 3:
            ip = (vl - 2) if a != 0 else ip
        elif op == 4:
            b ^= c
        elif op == 5:
            result.append(combo(vl) % 8)
        elif op == 6:
            b = a >> combo(vl)
        elif op == 7:
            c = a >> combo(vl)
        ip += 2
    
    return result

def convert(ins):
    result = 0
    for i in ins:
        result <<= 3
        result += i
    return result

result = compute(a)
target = ops
ins = []
i = 0
while target != result:
    while i < 8:
        a = (convert(ins) << 3) + i
        result = compute(a)
        if target[-len(result):] == result:
            ins.append(i)
            i = 0
            break
        i += 1
    if i == 8:
        i = ins.pop() + 1

print(convert(ins))