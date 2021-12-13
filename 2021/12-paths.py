import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from typing import List
from graph import Graph
from parse import parse, findall
from math import prod
from dataclasses import dataclass
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/12-input.txt').read().splitlines()

C = {}
for line in data:
    a, b, *_ = line.split('-')
    if a in C:
        C[a].add(b)
    else:
        C[a] = {b}
    if b in C:
        C[b].add(a)
    else:
        C[b] = {a}

print(C)

def go(path, visited, sols, twice):
    current = path[-1]
    if current == "end":
        sols.add(tuple(p for p in path))
        return
    if current.islower():
        visited = visited | {current}
    for node in C[current]:
        if node not in visited:
            go(path + [node], visited, sols, twice)
        elif not twice and node != "start":
            go(path + [node], visited, sols, True)

sols = set()
go(["start"], set(), sols, False)
print(len(sols))
