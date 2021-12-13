from collections import Counter
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
dirname = os.path.dirname(__file__)


def my_range(a, b):
    return range(a, b+1) if a <= b else range(a, b-1, -1)


def expand(a, b):
    if a[0] == b[0]:
        return [(a[0], y) for y in my_range(a[1], b[1])]
    elif a[1] == b[1]:
        return [(x, a[1]) for x in my_range(a[0], b[0])]

    return list(zip(my_range(a[0], b[0]), my_range(a[1], b[1])))


data = findall('{:d},{:d} -> {:d},{:d}', open(f'{dirname}/05-input.txt').read())
data = [((a, b), (c, d)) for a, b, c, d in data]
data = [expand(d[0], d[1]) for d in data]
data = Counter(c for d in data if d for c in d)
print(len([d for d in data.values() if d > 1]))
