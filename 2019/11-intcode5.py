from itertools import permutations
from collections import deque
from time import sleep

input = open('2019/11-input.txt').read()
data = {i: int(d) for i, d in enumerate(input.split(','))}

class IntCodeComputer:
    pc = 0
    data: list = None
    stdin: deque = None
    stdout = deque()
    state = 'not started'
    relative_base = 0

    def __init__(self, data, stdin):
        self.data = data
        self.stdin = stdin

    def read(self, i, mode):
        if mode == 0:
            return self.data.get(i, 0)
        elif mode == 1:
            return i
        elif mode == 2:
            return self.data[self.relative_base + i]
        else:
            assert False, f'read mode={mode} not recognised'

    def write(self, i, mode, value):
        if mode == 0:
            self.data[i] = value
        elif mode == 1:
            assert False, f'write mode={mode} not supported'
        elif mode == 2:
            self.data[self.relative_base + i] = value
        else:
            assert False, f'write mode={mode} not recognised'

    def resume(self):
        self.state = 'running'
        while self.state == 'running':
            self.__execute()
        return self.state

    def __pad(self, d):
        p = '0' * (5 - len(str(d))) + str(d)
        return map(int, (p[0], p[1], p[2], p[3:]))

    def __execute(self):
        data = self.data
        pc = self.pc
        m2, m1, m0, cmd = self.__pad(data[pc])
        if cmd == 1:
            a, b, c = data[pc + 1], data[pc + 2], data[pc + 3]
            self.write(c, m2, self.read(a, m0) + self.read(b, m1))
            self.pc += 4
        elif cmd == 2:
            a, b, c = data[pc + 1], data[pc + 2], data[pc + 3]
            self.write(c, m2, self.read(a, m0) * self.read(b, m1))
            self.pc += 4
        elif cmd == 3:
            if self.stdin:
                a = data[pc + 1]
                self.write(a, m0, self.stdin.popleft())
                self.pc += 2
            else:
                self.state = 'waiting for input'
        elif cmd == 4:
            a = data[pc + 1]
            self.stdout.append(self.read(a, m0))
            self.pc += 2
        elif cmd == 5:
            a, b = data[pc + 1], data[pc + 2]
            if self.read(a, m0):
                self.pc = self.read(b, m1)
            else:
                self.pc += 3
        elif cmd == 6:
            a, b = data[pc + 1], data[pc + 2]
            if not self.read(a, m0):
                self.pc = self.read(b, m1)
            else:
                self.pc += 3
        elif cmd == 7:
            a, b, c = data[pc + 1], data[pc + 2], data[pc + 3]
            self.write(c, m2, self.read(a, m0) < self.read(b, m1))
            self.pc += 4
        elif cmd == 8:
            a, b, c = data[pc + 1], data[pc + 2], data[pc + 3]
            self.write(c, m2, self.read(a, m0) == self.read(b, m1))
            self.pc += 4
        elif cmd == 9:
            a = data[pc + 1]
            self.relative_base += self.read(a, m0)
            self.pc += 2
        elif cmd == 99:
            self.state = 'halted'
        else:
            assert False, f'pc={pc}, cmd={cmd}'


def tadd(a, b):
    return tuple(c + d for c, d in zip(a, b))


computer = IntCodeComputer(data, deque())
point = (0, 0)
white_panels = {point}
painted_panels = set()
dir = (-1, 0)
while computer.state != 'halted':
    painted_panels.add(point)
    computer.stdin.append(int(point in white_panels))
    computer.resume()

    colour = computer.stdout.popleft()
    if colour:
        white_panels.add(point)
    else:
        white_panels.discard(point)

    rotation = computer.stdout.popleft()
    if rotation:
        dir = (dir[1], -dir[0])
    else:
        dir = (-dir[1], dir[0])

    point = tadd(point, dir)

minx = min(x for x, y in white_panels)
miny = min(y for x, y in white_panels)
maxx = max(x for x, y in white_panels)
maxy = max(y for x, y in white_panels)

for i in range(minx, maxx + 1):
    for j in range(miny, maxy + 1):
        if (i, j) in white_panels:
            print('#', end='')
        else:
            print(' ', end='')
    print()
