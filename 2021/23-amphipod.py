from collections import Counter, deque
from pprint import pprint
import os
from parse import parse, findall
import re
from copy import deepcopy
from heapq import heappush, heappop
from math import copysign
dirname = os.path.dirname(__file__)

style = 'HHJHJHJHJHH'
state = ('EEaEbEcEdEE', 'CDDA', 'DBCD', 'BABA', 'BCAC')
buckets = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
heap = [(0, state)]
visited = set()
heuristic = [{'A': 2 - i, 'B': 4 - i, 'C': 6 - i, 'D': 8 - i} for i in range(len(style))]


def add_state(state, s, i, cost):
    bucket = state[buckets[s]]
    *new_bucket, amphipod = bucket
    new_state = list(state)
    new_state[0] = state[0][:i] + amphipod + state[0][i + 1:]
    new_state[buckets[s]] = ''.join(new_bucket)
    heappush(heap, (cost, tuple(new_state)))


def add_exit_state(state, s, i, f):
    bucket = state[buckets[s.lower()]]
    new_bucket = bucket + s
    cost = (abs(heuristic[i][s]) + 4 - len(bucket)) * costs[s] + f
    new_state = list(state)
    new_state[0] = state[0][:i] + 'E' + state[0][i + 1:]
    new_state[buckets[s.lower()]] = new_bucket
    heappush(heap, (cost, tuple(new_state)))


def isEmpty(s):
    return s == 'E' or s.islower()


def can_exit(state, i, s):
    dir = int(copysign(1, heuristic[i][s]))
    i += dir
    while 0 <= i < len(state[0]) and state[0][i].upper() != s:
        if not isEmpty(state[0][i]):
            return False
        i += dir
    return all(s == t for t in state[buckets[s.lower()]])


def add_next_states(state, f):
    hallway = state[0]
    for i, s in enumerate(hallway):
        if s != 'E':
            if s.islower() and (bucket := state[buckets[s]]):
                if not all(s.upper() == b for b in bucket):
                    amphipod = bucket[-1]
                    j = i - 1
                    steps = (5 - len(bucket))
                    while j >= 0 and isEmpty(hallway[j]):
                        if hallway[j] == 'E':
                            add_state(state, s, j, (steps + i - j) * costs[amphipod] + f)
                        j -= 1
                    j = i + 1
                    while j < len(hallway) and isEmpty(hallway[j]):
                        if hallway[j] == 'E':
                            add_state(state, s, j, (steps + j - i) * costs[amphipod] + f)
                        j += 1
            elif s.isupper():
                if can_exit(state, i, s):
                    add_exit_state(state, s, i, f)


f = 0
while state[1:] != ('AAAA', 'BBBB', 'CCCC', 'DDDD'):
    f, state = heappop(heap)
    if state in visited:
        continue
    visited.add(state)
    add_next_states(state, f)

print(f, state)