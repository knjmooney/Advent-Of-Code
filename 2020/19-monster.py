import re
import os
from collections import Counter, namedtuple
from itertools import combinations, product
from pprint import pprint
from typing import List
from graph import Graph
from parse import parse, findall
from math import prod
from dataclasses import dataclass
from functools import cache
dirname = os.path.dirname(__file__)
data, messages = open(f'{dirname}/19-input.txt').read().split('\n\n')
data = {s[0]: s[1].replace('"', '') for d in data.splitlines() if (s := d.split(': '))}
messages = messages.splitlines()


def is_valid(alts):
    alt = alts.pop()
    seq = alt[0]
    message = alt[1]

    while True:
        while seq and message and not seq[0].isalpha():
            v = data[seq[0]]
            if '|' in v:
                a, b = v.split(' | ')
                alts.append((b.split() + seq[1:], message[:]))
                seq = a.split() + seq[1:]
            else:
                seq = v.split() + seq[1:]

        a = seq.pop(0)
        b = message.pop(0)
        if a != b:
            return False

        # We have a match if both are empty, or a miss if only one is empty
        if not seq or not message:
            return seq == message


def do_check(message):
    alts = [(['0'], list(message))]
    while alts:
        if is_valid(alts):
            return True
    return False


data['8'] = "42 | 42 8"
data['11'] = "42 31 | 42 11 31"
count = 0
for m in messages:
    r = do_check(m)
    if do_check(m):
        count += 1
print(count)
