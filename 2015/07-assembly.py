from collections import namedtuple
from time import sleep
from requests_cache import CachedSession
from parse import parse
from pprint import pprint

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/7/input', cookies=cookies)
    .content
    .decode()
    .splitlines()
)

to_proccess = (
    [{'op': 'SET', 'from': [p[0]], 'to': p[1]} for d in data if (p := parse('{:S} -> {}', d))] +
    [{'op': 'NOT', 'from': [p[0]], 'to': p[1]} for d in data if (p := parse('NOT {} -> {}', d))] +
    [{'op': p[1], 'from': [p[0], p[2]], 'to': p[3]} for d in data if (p := parse('{} {} {} -> {}', d))]
)

assert len(data) == len(to_proccess)

values = {}

def get_value(k):
    if k.isnumeric():
        return int(k)
    return values.get(k)


while 'a' not in values:
    for p in to_proccess:
        op, fm, to = p.values()
        if op == 'SET':
            if to == 'b':
                values[to] = 46065  # value of a from part 1
            elif (v := get_value(fm[0])) is not None:
                values[to] = v
        elif op == 'NOT':
            if (v := get_value(fm[0])) is not None:
                values[to] = v ^ 65535
        elif op == 'LSHIFT':
            if (a := get_value(fm[0])) is not None and (b := get_value(fm[1])) is not None:
                values[to] = a << b
        elif op == 'RSHIFT':
            if (a := get_value(fm[0])) is not None and (b := get_value(fm[1])) is not None:
                values[to] = a >> b
        elif op == 'AND':
            if (a := get_value(fm[0])) is not None and (b := get_value(fm[1])) is not None:
                values[to] = a & b
        elif op == 'OR':
            if (a := get_value(fm[0])) is not None and (b := get_value(fm[1])) is not None:
                values[to] = a | b
        else:
            assert False, f'{op} not recognised'

print(values['a'])
