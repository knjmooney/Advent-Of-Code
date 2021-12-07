from collections import Counter, namedtuple
from itertools import combinations
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
dirname = os.path.dirname(__file__)
data = [int(s) for s in open(f'{dirname}/10-input.txt').read().splitlines()]


data = [0] + sorted(data) + [max(data) + 3]
diff = [b - a for a, b in zip(data, data[1:])]
c = Counter(diff)

count = 1
if diff[0] == 1 and diff[1] == 1:
    count += count
if diff[0] == 1 and diff[1] == 1 and diff[2] == 1:
    count += count

for i in range(3, len(data)-1):
    if diff[i-3] == 1 and diff[i-2] == 1 and diff[i-1] == 1 and diff[i] == 1:
        count //= 4 
        count *= 7
    elif diff[i-1] == 1 and diff[i] == 1:
        count += count

print(count)
