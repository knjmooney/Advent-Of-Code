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
data = open(f'{dirname}/19-input.txt').read()
messages = data.split('\n\n')[1].splitlines()

def message(value):
    if '"' in value:
        return {'type': 'char', 'value': parse('"{}"', value)[0]}
    elif '|' in value:
        return {'type': 'or', 'value': [[int(c) for c in v.strip().split()] for v in value.split('|')]}
    else:
        return {'type': 'cat', 'value': [int(v) for v in value.split()]}


data = {p['key']: message(p['value']) for d in data.splitlines() if (p:=parse('{key:d}: {value}', d))}

@cache
def all_p(n):
    d = data[n]
    t = d['type']
    v = d['value']
    if t == 'char':
        return v
    elif t == 'or':
        a = tuple(all_p(x) for x in v[0])
        a = [''.join(x) for x in product(*a)]
        b = tuple(all_p(x) for x in v[1])
        b = [''.join(x) for x in product(*b)]
        return a + b
    else:
        r = tuple(all_p(x) for x in v)
        r = [''.join(x) for x in product(*r)]
        return r



def is_valid(n):


zero_ps = set(p for p in all_p(0))
print(sum(m in zero_ps for m in messages))
