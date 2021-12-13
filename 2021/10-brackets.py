import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/10-input.txt').read().splitlines()
# print(data)
corrupted = {')':0, '}':0, '>':0, ']':0}
open_to_close = {'(':')', '{':'}', '<':'>', '[':']'}
scores = []
for id, line in enumerate(data):
    line = [c for c in line]
    unmatched = [line.pop(0)]
    assert unmatched[0] in open_to_close.keys()
    corrupt = False
    while len(line):
        # print(id, unmatched)
        token = line.pop(0)
        if token in open_to_close.keys():
            unmatched.append(token)
            continue
        assert token in open_to_close.values()
        open_token = unmatched.pop()
        if open_to_close[open_token] == token:
            continue
        corrupted[token] += 1
        corrupt = True
        # print(id, 'corrupted')
        break
    if not corrupt:
        points = {'(':1, '{':3, '<':4, '[':2}
        score = 0
        for token in reversed(unmatched):
            score *= 5
            score += points[token]
        scores.append(score)

print(corrupted)
print(corrupted[')'] * 3 + corrupted[']'] * 57 + corrupted['}'] * 1197 + corrupted['>'] * 25137)
print(sorted(scores)[len(scores)//2])


