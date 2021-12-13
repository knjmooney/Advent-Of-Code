import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = [int(d) for d in open(f'{dirname}/07-input.txt').read().split(',')]

# data = [16,1,2,0,4,2,7,1,2,14]
mina = min(data)
maxa = max(data)
sums = [(i, sum((abs(d - i) * (abs(d-i) + 1)) // 2 for d in data)) for i in range(mina, maxa + 1)]
print(sums)
print(min(sums, key=lambda t: t[1]))