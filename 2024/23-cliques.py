'''
Finding cliques in a graph. There's likely to be much better algorithms, but I
wanted to come up with one myself. 
'''

from requests_cache import CachedSession
from collections import defaultdict, Counter
from heapq import heappop, heappush
from functools import cache
from itertools import product
from parse import parse

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/23/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

graph = defaultdict(set)
for l in data.splitlines():
    a, b = parse('{}-{}', l).fixed
    graph[a].add(b)
    graph[b].add(a)

cliques = {}
for a in graph:
    cliques[frozenset([a])] = graph[a]

while True:
    new_cliques = {}
    for clique in cliques:
        for node in cliques[clique]:
            shared = cliques[clique] & graph[node]
            if shared:
                new_cliques[clique | frozenset([node])] = shared
    if not new_cliques:
        break
    cliques = new_cliques

print(','.join(sorted(v for x in cliques.values() for v in x)))

