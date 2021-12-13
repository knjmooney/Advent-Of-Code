import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = parse("{}\n\nyour ticket:\n{}\n\nnearby tickets:\n{}", open(f'{dirname}/16-input.txt').read())
constraints, your_ticket, nearby_tickets = data[0], data[1], data[2]
constraints = [parse("{}: {:d}-{:d} or {:d}-{:d}", c) for c in constraints.splitlines()]
all_nearby = [[int(x) for x in n.split(',')] for n in nearby_tickets.splitlines()]
invalid_values = [n for nearby in all_nearby for n in nearby if not any(c[1] <= n <= c[2] or c[3] <= n <= c[4] for c in constraints)]
print(sum(invalid_values))
all_valid = [nearby for nearby in all_nearby if not any(n in invalid_values for n in nearby)]
print(len(all_nearby))
print(len(all_valid))

L = len(constraints)
print(L)
cs = constraints
vs = all_valid
potentials = [(j, [i for i in range(L) if all(cs[i][1] <= v[j] <= cs[i][2] or cs[i][3] <= v[j] <= cs[i][4] for v in vs)]) for j in range(L)]
# print(cs)
# print(vs)
potentials = sorted(potentials, key=lambda t: len(t[1]))
seen = set()
result = []
for id, p in potentials:
    p = set(p)
    v = p - seen
    assert len(v) == 1
    v = v.pop()
    seen.add(v)
    result.append((id, v))

print(prod([int(your_ticket.split(',')[r[0]]) for r in result if 'departure' in cs[r[1]][0]]))


def solve(n_id, result):
    # print(result)
    if len(result) == len(constraints):
        return result

    for c_id in potentials[n_id]:
        c = constraints[c_id]
        if c_id not in result:
            r = solve(n_id + 1, result + [c_id])
            if r:
                return r
    return None

# print(solve(0, []))