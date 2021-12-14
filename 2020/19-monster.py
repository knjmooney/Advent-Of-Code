import re
import os
from collections import Counter, namedtuple
from itertools import combinations, product
from pprint import pprint
from typing import List
from graph import Graph
from parse import parse, findall
from math import prod
from dataclasses import dataclass
from functools import cache
dirname = os.path.dirname(__file__)
data2, messages = open(f'{dirname}/19-input.txt').read().split('\n\n')
data2 = {s[0]: s[1].replace('"','') for d in data2.splitlines() if (s := d.split(': '))}
messages = messages.splitlines()


def all_p(n):
    "I generated all possibilities for part 1"
    d = data[n]
    t = d['type']
    v = d['value']
    if t == 'char':
        return v
    elif t == 'or':
        a = tuple(all_p(x) for x in v[0])
        a = [''.join(x) for x in product(*a)] if a[0] is not None else []
        b = tuple(all_p(x) for x in v[1])
        b = [''.join(x) for x in product(*b)] if b[0] is not None else []
        return a + b
    else:
        r = tuple(all_p(x) for x in v)
        r = [''.join(x) for x in product(*r)] if r[0] is not None else []
        return r


def is_valid(alts):
    alt = alts.pop()
    seq = alt[0]
    message = alt[1]

    while True:
        while seq and message and not seq[0].isalpha():
            v = data2[seq[0]]
            if '|' in v:
                a, b = v.split(' | ')
                alts.append((b.split() + seq[1:], message[:]))
                seq = a.split() + seq[1:]
            else:
                seq = v.split() + seq[1:]

        a = seq.pop(0)
        b = message.pop(0)
        if a != b:
            return False

        # We have a match if both are empty, or a miss if only one is empty
        if not seq or not message:
            return seq == message


def do_check(message):
    alts = [(['0'], list(message))]
    while alts:
        if is_valid(alts):
            return True
    return False


data2['8'] = "42 | 42 8"
data2['11'] = "42 31 | 42 11 31"
count = 0
for m in messages:
    r = do_check(m)
    if do_check(m):
        count += 1
print(count)