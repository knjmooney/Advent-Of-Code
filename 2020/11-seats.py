from collections import Counter, namedtuple
from itertools import combinations
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
dirname = os.path.dirname(__file__)
seats = open(f'{dirname}/11-input.txt').read().splitlines()
H = len(seats)
W = len(seats[0])

def valid(i, j):
    return 0 <= i < H and 0 <= j < W

def visible_neighbour(i, j, i_dir, j_dir):
    i += i_dir
    j += j_dir
    while valid(i, j):
        if seats[i][j] == 'L' or seats[i][j] == '#':
            return (i, j)
        i += i_dir
        j += j_dir
    return None

def update(seats, i, j):
    nns = [nn for i_dir in range(-1, 2) for j_dir in range(-1, 2)
           if (i_dir or j_dir) and (nn := visible_neighbour(i, j, i_dir, j_dir))]
    if seats[i][j] == 'L':
        if all(seats[nn[0]][nn[1]] == 'L' or seats[nn[0]][nn[1]] == '.' for nn in nns):
            return '#'
        return 'L'
    if seats[i][j] == '#':
        if sum(seats[nn[0]][nn[1]] == '#' for nn in nns) > 4:
            return 'L'
        return '#'
    return '.'


old_seats = seats[:]
seats = [''.join(update(seats, i, j) for j in range(W)) for i in range(H)]
while old_seats != seats:
    old_seats = seats[:]
    seats = [''.join(update(seats, i, j) for j in range(W)) for i in range(H)]
print(sum(seats[i][j] == '#' for i in range(H) for j in range(W)))
