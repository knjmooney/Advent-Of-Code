from collections import Counter
import re
from pprint import pprint
import os
dirname = os.path.dirname(__file__)

input = open(f'{dirname}/04-input.txt').read().split("\n\n")
numbers = [int(n) for n in input[0].split(',')]
boards = [[[int(n) for n in r.split()]
           for r in b.splitlines()] for b in input[1:]]

rcs = [[r for r in b] + [c for c in zip(*b)] for b in boards]
ids = [[[(n, numbers.index(n)) for n in r] for r in b] for b in rcs]
maxes = [[(r, max(r, key=lambda t: t[1])) for r in b] for b in ids]
mins = [min(b, key=lambda t: t[1][1]) for b in maxes]

the_min = max(mins, key=lambda t: t[1][1])
min_board_id = mins.index(the_min)
winning_board = boards[min_board_id]
min_number_id = the_min[1][1]
print(the_min[1][0] * sum([n for r in winning_board for n in r if n not in numbers[:min_number_id + 1]]))
