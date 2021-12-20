import re
import os
from collections import Counter, namedtuple
from itertools import combinations
from pprint import pprint
from graph import Graph
from parse import parse, findall
from math import prod
from bisect import bisect_left, insort
dirname = os.path.dirname(__file__)
data = open(f'{dirname}/16-input.txt').read().strip()
data = ''.join([format(int(d, 16), f'0{4}b') for d in data])

total_version = 0

def parse_literal(i):
    number = ''
    while True:
        if data[i] == '1':
            i += 1
            number += data[i:i + 4]
            i += 4
        else:
            i += 1
            number += data[i:i + 4]
            i += 4
            break
    return (int(number, 2), i)

def parse_operator(i):
    len_type_id = data[i]
    i += 1
    values = []
    if len_type_id == '0':
        total_len = int(data[i:i + 15], 2)
        i += 15
        seen_len = 0
        while seen_len < total_len:
            start = i
            value, i = parse_packet(i)
            values.append(value)
            seen_len += i - start
        assert seen_len == total_len
    else:
        num_packets = int(data[i:i + 11], 2)
        i += 11
        for count in range(num_packets):
            value, i = parse_packet(i)
            values.append(value)

    return (values, i)

def parse_packet(start):
    global total_version
    version = int(data[start:start + 3], 2)
    typeid = int(data[start + 3:start + 6], 2)

    total_version += version

    if typeid == 4:
        literal, end = parse_literal(start + 6)
        return (literal, end)
    else:
        values, end = parse_operator(start + 6)
        value = None
        if typeid == 0:
            value = sum(values)
        elif typeid == 1:
            value = prod(values)
        elif typeid == 2:
            value = min(values)
        elif typeid == 3:
            value = max(values)
        elif typeid == 5:
            assert len(values) == 2
            value = values[0] > values[1]
        elif typeid == 6:
            assert len(values) == 2
            value = values[0] < values[1]
        elif typeid == 7:
            assert len(values) == 2
            value = values[0] == values[1]

        assert value is not None
        return (value, end)


print('length:', len(data))
print('value:', parse_packet(0)[0])
print('total version:', total_version)
