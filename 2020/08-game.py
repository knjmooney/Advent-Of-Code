from collections import Counter, namedtuple
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
dirname = os.path.dirname(__file__)


def play(data):
    acc = 0
    pc = 0
    executed = set()
    while pc not in executed and pc != len(data):
        executed.add(pc)
        if data[pc]['token'] == 'jmp':
            pc += data[pc]['arg']
            continue
        elif data[pc]['token'] == 'acc':
            acc += data[pc]['arg']
        pc += 1
    return (pc == len(data), acc)


data = [parse('{token} {arg:d}', s).named for s in open(f'{dirname}/08-input.txt').read().splitlines()]

nop_ids = [i for i, x in enumerate(data) if x['token'] == 'nop']
jmp_ids = [i for i, x in enumerate(data) if x['token'] == 'jmp']

for nop_id in nop_ids:
    new_data = data[:]
    new_data[nop_id] = {'token': 'jmp', 'arg': data[nop_id]['arg']} 
    complete, acc = play(new_data)
    if complete:
        print('Yeah', acc)
    
for jmp_id in jmp_ids:
    new_data = data[:]
    new_data[jmp_id] = {'token': 'nop', 'arg': data[nop_id]['arg']} 
    complete, acc = play(new_data)
    if complete:
        print('Yeah', acc)
