'''
I thought part 2 was the hardest in terms of problem solving. It required
the worry level constrained. I initially was using the mod of each monkey's
divisor, but that didn't work because you would then pass the item onto another
monkey and the divisibility check was then broken. The trick was to use the 
product of the divisors.
'''

from collections import deque, namedtuple
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/11/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .split('\n\n')
)

def parse_monkey(monkey):
    monkey = monkey.splitlines()
    return {
        'items': [int(x) for x in parse('  Starting items: {}', monkey[1]).fixed[0].split(',')],
        **parse('  Operation: new = {op}', monkey[2]).named,
        **parse('  Test: divisible by {divby:d}', monkey[3]).named,
        **parse('    If true: throw to monkey {true:d}', monkey[4]).named,
        **parse('    If false: throw to monkey {false:d}', monkey[5]).named,
        'inspected': 0
    }


monkeys = [parse_monkey(d) for d in data]

# eval is slow, but this speeds it up (~4)
for monkey in monkeys:
    monkey['op'] = compile(monkey['op'], 'doop', 'eval')

mod = prod(monkey['divby'] for monkey in monkeys)
for round in range(10000):
    for i, monkey in enumerate(monkeys):
        while monkey['items']:
            monkey['inspected'] += 1
            old = monkey['items'].pop(0)
            new = eval(monkey['op']) % mod
            if new % monkey['divby'] == 0:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)

inspects = sorted(m['inspected'] for m in monkeys)
print(inspects[-2] * inspects[-1])
