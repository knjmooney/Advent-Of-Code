from itertools import permutations
from collections import defaultdict, deque
from time import sleep
import os
from pynput import keyboard

input = open('2019/14-test-input.txt').read().splitlines()

data = [d.split(' => ') for d in input]
data = [(a.split(', '), b.split()) for a,b in data]
data = {b[1]: [int(b[0]), {f: int(e) for e, f in (c.split() for c in a)}] for a, b in data}

def is_complete(node):
    return len(node[1]) == 1 and 'ORE' in node[1].values()


spares = defaultdict(int)
while not is_complete(data['FUEL']):
    for ingredient, amount in data['FUEL'][1].copy().items():
        spares[ingredient] -= min(spares[ingredient], amount)
        amount -= min(spares[ingredient], amount)
        
    break