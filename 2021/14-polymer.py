import re
import os
from collections import Counter, namedtuple
from itertools import combinations, product
from pprint import pprint
from typing import List
from graph import Graph
from parse import parse, findall
from math import prod
from dataclasses import dataclass
from functools import cache
dirname = os.path.dirname(__file__)
polymer, rules = open(f'{dirname}/14-input.txt').read().split('\n\n')
rules = {tuple(v[0]): v[1] for r in rules.splitlines() if (v := r.split(' -> '))}

counts = Counter(zip(polymer, polymer[1:]))
for _ in range(40):
    counts = sum((Counter({(p[0], rules[p]): c, (rules[p], p[1]): c}) for p, c in counts.items()), Counter())

letter_counts = sum((Counter({p[0] : c}) for p, c in counts.items()), Counter())
letter_counts[polymer[-1]] += 1
print(letter_counts.most_common()[0][1] - letter_counts.most_common()[-1][1])
