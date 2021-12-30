from collections import Counter, deque
from pprint import pprint
import os
from parse import parse, findall
import re
dirname = os.path.dirname(__file__)


def compute(data, z, w):
    regs = {'x': 0, 'y': 0, 'z': z, 'w': int(w)}
    pc = 0
    while pc != len(data):
        d = data[pc].split()
        cmd = d[0]
        out = d[1]
        if cmd == 'add':
            regs[out] += regs[d[2]] if d[2].isalpha() else int(d[2])
            if d[2][0] == '-' and w != regs['x']:
                return z, False
        elif cmd == 'mul':
            regs[out] *= regs[d[2]] if d[2].isalpha() else int(d[2])
        elif cmd == 'div':
            regs[out] //= regs[d[2]] if d[2].isalpha() else int(d[2])
        elif cmd == 'mod':
            regs[out] %= regs[d[2]] if d[2].isalpha() else int(d[2])
        elif cmd == 'eql':
            regs[out] = int(regs[out] == (regs[d[2]] if d[2].isalpha() else int(d[2])))
        else:
            assert False, f'not an instruction {cmd}'
        pc += 1
    return regs['z'], True


data = open(f'{dirname}/24-input.txt').read()
data = data.split('inp w\n')
data = [d.splitlines() for d in data if d]

this = [1]
zs = [0]
i = 0
while i < 14:
    t = this[i]
    d = data[i]
    z = zs[i]
    z, success = compute(d, z, t)
    if not success:
        while this[i] == 9:
            i -= 1
            this.pop()
            zs.pop()
        this[i] += 1
    else:
        this.append(1)
        zs.append(z)
        i += 1


print(''.join(str(t) for t in this[:14]))