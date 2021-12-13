import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/18-input.txt').read().splitlines()

def evaluate_p1(calc):
    a = calc[0]
    for j in range(1, len(calc), 2):
        op = calc[j]
        b = calc[j+1]
        a = eval(f'{a} {op} {b}')
    return a

def evaluate_p2(calc):
    while '+' in calc:
        id = calc.index('+')
        out = str(eval(''.join(calc[id-1:id+2])))
        calc = calc[:id-1] + [out] + calc[id+2:]

    return str(eval(''.join(calc)))

def parse(data):
    stack = [[]]
    for i in range(len(data)):
        if data[i] == '(':
            stack.append([])
        elif data[i] == ')':
            calc = stack.pop()
            stack[-1].append(evaluate_p2(calc))
        elif data[i] == ' ':
            pass
        else:
            stack[-1].append(data[i])
    return(int(evaluate_p2(stack.pop())))

print(sum([parse(d) for d in data]))