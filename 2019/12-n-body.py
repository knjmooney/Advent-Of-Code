from itertools import permutations
from collections import deque
from time import sleep
from parse import parse
from pprint import pprint
from math import lcm


class planet:
    def __init__(self, pos):
        self.pos = list(pos)
        self.vel = [0, 0, 0]

    def __repr__(self):
        return f'pos: {self.pos}, vel: {self.vel}'

    def __hash__(self) -> int:
        return hash((tuple(self.pos), tuple(self.vel)))

    def energy(self):
        potential = sum(abs(p) for p in self.pos)
        kinetic = sum(abs(v) for v in self.vel)
        return potential * kinetic


data = [planet(parse('<x={:d}, y={:d}, z={:d}>', d).fixed) for d in open('2019/12-input.txt').read().splitlines()]

states = set()
iterx = 0
while tuple(data) not in states:
    iterx += 1
    states.add(tuple(data))
    for curr in data:
        for other in data:
            curr.vel[0] += curr.pos[0] < other.pos[0]
            curr.vel[0] -= curr.pos[0] > other.pos[0]

    for curr in data:
        curr.pos[0] += curr.vel[0]

states = set()
itery = 0
while tuple(data) not in states:
    itery += 1
    states.add(tuple(data))
    for curr in data:
        for other in data:
            curr.vel[1] += curr.pos[1] < other.pos[1]
            curr.vel[1] -= curr.pos[1] > other.pos[1]

    for curr in data:
        curr.pos[1] += curr.vel[1]

states = set()
iterz = 0
while tuple(data) not in states:
    iterz += 1
    states.add(tuple(data))
    for curr in data:
        for other in data:
            curr.vel[2] += curr.pos[2] < other.pos[2]
            curr.vel[2] -= curr.pos[2] > other.pos[2]

    for curr in data:
        curr.pos[2] += curr.vel[2]

print(lcm(iterx, itery, iterz))
