import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = [0, 12, 6, 13, 20, 1, 17]
data, last_num = data[:-1], data[-1]
called = {d: e for e, d in enumerate(data, 1)}
for i in range(len(data) + 1, 30000000):
    if last_num in called:
        this_num = i - called[last_num]
    else:
        this_num = 0
    called[last_num] = i
    last_num = this_num

print(last_num)
