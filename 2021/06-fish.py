from collections import Counter, namedtuple
from itertools import combinations
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
dirname = os.path.dirname(__file__)
fishes = [int(s) for s in open(f'{dirname}/06-input.txt').read().split(',')]


def fish(fishes, days):
    counts = Counter(fishes)
    for d in range(days):
        counts = Counter({((key - 1) % 9): value for key, value in counts.items()})
        counts[6] += counts[8]
    return sum(c for c in counts.values())


print(fish([3, 4, 3, 1, 2], 18))
print(fish(fishes, 80))
print(fish(fishes, 256))
