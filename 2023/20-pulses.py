"""
Old code, not sure if it works.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter, defaultdict, deque
from itertools import (
    combinations_with_replacement,
    cycle,
    chain,
    repeat,
    islice,
    combinations,
    count,
)
from math import lcm, prod
import functools
import sys
from heapq import heappop, heappush


data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/20/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

# data = '''broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a'''

# data = '''broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output'''

nodes = {}
d : str
for d in data.splitlines():
    l, r = d.split(' -> ')
    t = l[0]
    state = None if t == 'b' else False if t == '%' else defaultdict(bool)
    nodes[l.lstrip('%').lstrip('&')] = [
        t, 
        r.split(', '),
        state
    ]

inputs = defaultdict(list)
for key, (_, outputs, _) in nodes.items():
    for output in outputs:
        inputs[output].append(key)
        if output not in nodes:
            continue
        t, _, state = nodes[output] 
        if t == '&':
            state[key] = False

def processQueue():
    while queue:
        id, hilo, src = queue.popleft()

        if id == 'rx' and hilo == False:
            print('rx received', hilo)

        if id not in nodes:
            continue

        t, nextNodes, state = nodes[id]
        if t == '%':
            if hilo == True:
                continue
            nodes[id][2] = not state
            # print(f'{id:5} {not state:<3} {counts} {nextNodes}')
            # counts[not state] += len(nextNodes)
            queue.extend((n, not state, id) for n in nextNodes)
        elif t == '&':
            state[src] = hilo
            # print(f'{id:5} {not all(state.values()):<3} {counts} {nextNodes} {dict(state)}')
            # counts[not all(state.values())] += len(nextNodes)
            if len(state) > 1 and all(state.values()):
                print(i, id, state.values())
            queue.extend((n, not all(state.values()), id) for n in nextNodes)
        else:
            assert False

def doPrint(id):
    for node in nodes[id][2].values():
        print(i, id, dict(nodes[id][2]), flush=True)


watch = []
for inpt in inputs['rx']:
    for inpt2 in inputs[inpt]:
        for inpt3 in inputs[inpt2]:
            watch.extend(nodes[inpt3][2])

# print(watch)
# for w in watch:
#     print(nodes[w][0], nodes[w][2])


counts = defaultdict(list)
results = defaultdict(int)
for i in range(1, 80000):
    # counts[0] += 1 + len(nodes['broadcaster'][1])
    queue : deque = deque((n, False, 'broadcaster') for n in nodes['broadcaster'][1])
    processQueue()
    for w in watch:
        if nodes[w][2]:
            counts[w].append(i)

    # doPrint('jd')
    # doPrint('jd')

# for k, v in counts.items():
    # print(k, v[0], v[-1])

# print(counts, counts[0] * counts[1])