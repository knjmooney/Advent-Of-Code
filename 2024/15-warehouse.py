'''
This was a fun one, just a matter of coding all the rules. Plenty of
opportunities for typos though.
'''

from requests_cache import CachedSession
from collections import defaultdict

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/15/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

map, route = data.split('\n\n')

data = {}
for i, row in enumerate(map.splitlines()):
    for j, e in enumerate(row):
        if e == 'O':
            data[i + (2 * j + 0) * 1j] = '['
            data[i + (2 * j + 1) * 1j] = ']'
        elif e == '@':
            data[i + (2 * j + 0) * 1j] = '@'
            data[i + (2 * j + 1) * 1j] = '.'
        else:
            data[i + (2 * j + 0) * 1j] = e
            data[i + (2 * j + 1) * 1j] = e

route = route.replace('\n','')
dirs = {'v': 1, '^': -1, '>': 1j, '<': -1j}

def print_map():
    h, w = max((int(e.real) + 1, int(e.imag) + 1) for e in data)
    for i in range(h):
        print(''.join(data[i + j * 1j] for j in range(w)))

def can_push(p, dir):
    if p not in data:
        return False
    
    e = data[p]
    if e == '#':
        return False

    if e == '.':
        return True
    
    nextp = p + dir
    if e == '[':
        if dir == 1j:
            assert(data[nextp] == ']')
            return can_push(nextp + dir, dir)
        if dir == -1j:
            assert False
        assert data[p + 1j] == ']'
        return can_push(nextp, dir) and can_push(nextp + 1j, dir)

    if e == ']':
        if dir == -1j:
            assert(data[nextp] == '[')
            return can_push(nextp + dir, dir)
        if dir == 1j:
            assert False
        assert data[p - 1j] == '['
        return can_push(nextp, dir) and can_push(nextp - 1j, dir)

    assert False


def do_push(p, dir):
    if p not in data:
        assert False
    
    e = data[p]
    if e == '#':
        assert False

    if e == '.':
        return

    nextp = p + dir
    if e == '[':
        if dir == 1j:
            assert(data[nextp] == ']')
            do_push(nextp + dir, dir)
            data[p] = '.'
            data[nextp] = '['
            data[nextp + dir] = ']'
            return
        if dir == -1j:
            assert False
        assert data[p + 1j] == ']'
        do_push(nextp, dir)
        do_push(nextp + 1j, dir)
        data[p] = '.'
        data[p + 1j] = '.'
        data[nextp] = '['
        data[nextp + 1j] = ']'
        return

    if e == ']':
        if dir == -1j:
            assert(data[nextp] == '[')
            do_push(nextp + dir, dir)
            data[p] = '.'
            data[nextp] = ']'
            data[nextp + dir] = '['
            return
        if dir == 1j:
            assert False
        assert data[p - 1j] == '['
        do_push(nextp, dir)
        do_push(nextp - 1j, dir)
        data[p] = '.'
        data[p - 1j] = '.'
        data[nextp] = ']'
        data[nextp - 1j] = '['
        return

    assert False


def walk():

    p = list(data.keys())[list(data.values()).index('@')]

    for dirChar in route:
        dir = dirs[dirChar]
        nextp = p + dir
        if can_push(nextp, dir):
            do_push(nextp, dir)
            data[p], data[nextp] = '.', '@'
            p = nextp

walk()

result = 0
for k, v in data.items():
    if v == '[':
        result += int(k.real) * 100 + int(k.imag)

print(result)