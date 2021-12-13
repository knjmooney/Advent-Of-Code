import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = [parse("{token} = {value}", d).named.values() for d in open(f'{dirname}/14-input.txt').read().splitlines()]

def expand(masked_addr):
    if 'X' in masked_addr:
        return expand(masked_addr.replace('X', '1', 1)) + expand(masked_addr.replace('X', '0', 1))
    return [masked_addr]


memory = dict()
for token, value in data:
    if token == 'mask':
        mask = value
    else:
        addr = parse('mem[{:d}]', token)[0]
        addr_bin = format(addr, '036b')
        masked_addr = ''.join(a if m == '0' else '1' if m == '1' else 'X' for m, a in zip(mask, addr_bin))
        for a in expand(masked_addr):
            memory[a] = int(value)


print(sum(memory.values()))
