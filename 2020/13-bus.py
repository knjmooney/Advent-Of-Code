import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/13-input.txt').read().splitlines()
buses = [(id, int(b)) for id, b in enumerate(data[1].split(',')) if b != 'x']

def inverse(a, n):
    t, newt = 0, 1
    r, newr = n, a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    assert not (r > 1)
    if t < 0:
        t += n

    return t

def crt(As, Ms):
    "Chinese remainder theorem"
    assert len(As) == len(Ms)
    M = prod(Ms)
    Zs = [M // m for m in Ms]
    Ys = [inverse(z, m) for z, m in zip(Zs, Ms)]
    Ws = [(y * z) for y, z, m in zip(Ys, Zs, Ms)]
    return sum([a * w for a, w in zip(As, Ws)]) % M


As = [(bus - id) % bus for id, bus in buses]
Ms = [bus for _, bus in buses]
print(crt(As, Ms))
