from itertools import permutations
from collections import deque
from fractions import Fraction
from math import atan2, pi
from copy import deepcopy

data = [list(d) for d in open('2019/10-input.txt').read().splitlines()]

H = len(data)
W = len(data[0])

def tadd(a, b):
    return tuple(c + d for c, d in zip(a, b))


line_of_sights = {Fraction(i, j).as_integer_ratio() for i in range(H) for j in range(W) if j != 0}
line_of_sights.add((1, 0))
for m in deepcopy(line_of_sights):
    line_of_sights.add((m[0] * -1, m[1] * +1))
    line_of_sights.add((m[0] * +1, m[1] * -1))
    line_of_sights.add((m[0] * -1, m[1] * -1))

result = {}
for i in range(H):
    for j in range(W):
        curr = (i, j)
        if data[i][j] != '#':
            continue
        result[curr] = 0
        for m in line_of_sights:
            other = tadd(curr, m)
            while 0 <= other[0] < H and 0 <= other[1] < W:
                if data[other[0]][other[1]] == '#':
                    result[curr] += 1
                    break
                other = tadd(other, m)

def start_destroying(source):
    global line_of_sights
    line_of_sights = sorted(line_of_sights, key=lambda p: (atan2(-p[1], p[0]) + pi) % (2 * pi))
    count = 0
    while True:
        for m in line_of_sights:
            other = tadd(source, m)
            while 0 <= other[0] < H and 0 <= other[1] < W:
                if data[other[0]][other[1]] == '#':
                    data[other[0]][other[1]] = '.'
                    count += 1
                    if count == 200:
                        return other
                    break
                other = tadd(other, m)


max_p = max(result, key=lambda key: result[key])
print(max_p, result[max_p])
print(start_destroying(max_p))
