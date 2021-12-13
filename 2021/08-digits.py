import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = [d.split('|') for d in open(f'{dirname}/08-input.txt').read().splitlines()]
data = [[io.strip().split() for io in d] for d in data]
inputs, outputs = list(zip(*data))

n = [0] * 10
ans = []
for input, output in data:
    input = [set(i) for i in input]
    n[1] = set(next(i for i in input if len(i) == 2))
    n[7] = set(next(i for i in input if len(i) == 3))
    n[4] = set(next(i for i in input if len(i) == 4))
    n[8] = set(next(i for i in input if len(i) == 7))
    a = (n[7] - n[1]).pop()
    n[9] = next(i for i in input if (n[4] | n[7]) < i and i != n[8])
    e = (n[8] - n[9]).pop()
    g = (n[9] - n[4] - {a}).pop()
    n[2] = next(i for i in input if len(i) == 5 and e in i)
    c = (n[1] & n[2]).pop()
    d = (n[2] - {a, c, e, g}).pop()
    f = (n[1] - {c}).pop()
    b = (n[4] - {d, c, f}).pop()
    n[0] = next(i for i in input if i == {a, b, c, e, f, g})
    n[3] = next(i for i in input if i == {a, c, d, f, g})
    n[5] = next(i for i in input if i == {a, b, d, f, g})
    n[6] = next(i for i in input if i == {a, b, d, e, f, g})
    ans.append(int(''.join([str(n.index(set(o))) for o in output])))
print(sum(ans))