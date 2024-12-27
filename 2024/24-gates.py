'''
That was tricky. Mostly manual inspection of the input once an assertion was
broken. I had to find an RNG seed that would generate two numbers that forced
extra failures.
'''

from requests_cache import CachedSession
from collections import defaultdict, namedtuple
from parse import parse
from fractions import Fraction as frac

import json
import math
import re
import random

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/24/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

values, actions = data.split('\n\n')

values = {k: int(v) for p in values.splitlines() for k, v in [parse('{}: {:d}', p).fixed]}
actions = actions.splitlines()

def compute(actions):
    while actions:
        unused_actions = []
        for action in actions:
            a, op, b, r = parse('{} {} {} -> {}', action).fixed
            if a not in values or b not in values:
                unused_actions.append(action)
            elif op == 'AND':
                values[r] = values[a] & values[b]
            elif op == 'OR':
                values[r] = values[a] | values[b]
            elif op == 'XOR':
                values[r] = values[a] ^ values[b]
        assert actions != unused_actions
        actions = unused_actions

def compute_r(reg, depth=0):
    if reg.startswith('x') or reg.startswith('y'):
        return values[reg]

    a_s, op, b_s = action_tree[reg]
    a = compute_r(a_s, depth + 1)
    b = compute_r(b_s, depth + 1)
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'XOR':
        return a ^ b

    assert False

def compute_debug(reg, depth=0):
    if reg.startswith('x') or reg.startswith('y'):
        return values[reg]

    a_s, op, b_s = action_tree[reg]
    a = compute_debug(a_s, depth + 1)
    b = compute_debug(b_s, depth + 1)
    if depth == 0:
        assert op == 'XOR', depth
    elif depth % 2 == 0:
        assert op == 'AND', depth
    else:
        assert op == 'XOR' or op == 'OR' or a_s.endswith('00'), depth

    if op == 'AND':
        print(reg, a_s, b_s, op, a & b, depth)
        return a & b
    elif op == 'OR':
        print(reg, a_s, b_s, '', op, a & b, depth)
        return a | b
    elif op == 'XOR':
        print(reg, a_s, b_s, op, a & b, depth)
        return a ^ b

    assert False

def print_r(reg, depth = 0):
    a, op, b = action_tree[reg]

    if a.startswith('x') or a.startswith('y'):
        return [(depth, *reversed(sorted((a, op, b))))]

    return [*print_r(a, depth + 1), *print_r(b, depth + 1)]

action_tree = {}
for action in actions:
    a, op, b, r = parse('{} {} {} -> {}', action).fixed
    assert r not in action_tree
    action_tree[r] = (a, op, b)


def swap(a, b):
    action_tree[a], action_tree[b] = action_tree[b], action_tree[a]

swap('mkk', 'z10')
swap('qbw', 'z14')
swap('cvp', 'wjb')
swap('z34', 'wcb')

random.seed(2)

for k in values:
    values[k] = random.randint(0, 1)

x = sum(v * 1 << int(k[1:]) for k, v in values.items() if k.startswith('x'))
y = sum(v * 1 << int(k[1:]) for k, v in values.items() if k.startswith('y'))
z = sum(compute_r(k) * 1 << int(k[1:]) for k, v in action_tree.items() if k.startswith('z'))
assert x + y == z, f'{x}, {y}, {z}'

print(compute_debug('z02'))

print('', bin(x))
print('', bin(y))
print(bin(z))
expected = x + y
print(bin(expected))
print([i for i, (a, b) in enumerate(zip(reversed(bin(z)), reversed(bin(expected)))) if a != b])



print(','.join(sorted(['mkk', 'z10', 'qbw', 'z14', 'cvp', 'wjb', 'z34', 'wcb'])))