from itertools import permutations
from collections import deque

input = open('2019/09-input.txt').read()
# input = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
data = {i: int(d) for i, d in enumerate(input.split(','))}

def pad(d):
    p = '0' * (5 - len(str(d))) + str(d)
    return map(int, (p[0], p[1], p[2], p[3:]))

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

    def __execute(self):
        data = self.data
        pc = self.pc
        m2, m1, m0, cmd = pad(data[pc])
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


computer = IntCodeComputer(data, deque([2]))
computer.resume()
print(computer.state, computer.stdout)
