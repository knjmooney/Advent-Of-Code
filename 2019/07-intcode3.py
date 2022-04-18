from itertools import permutations
from collections import deque

data = [int(d) for d in open('2019/07-input.txt').read().split(',')]

def pad(d):
    p = '0' * (5 - len(str(d))) + str(d)
    return map(int, (p[0], p[1], p[2], p[3:]))

class IntCodeComputer:
    pc = 0
    data: list = None
    stdin: deque = None
    stdout = deque()
    state = 'not started'

    def __init__(self, data, stdin):
        self.data = data
        self.stdin = stdin

    def read(self, data, i, immediate_mode):
        if immediate_mode:
            return i
        else:
            return data[i]

    def resume(self):
        self.state = 'running'
        while self.state == 'running':
            self.execute()
        return self.state

    def execute(self):
        data = self.data
        pc = self.pc
        m2, m1, m0, cmd = pad(data[pc])
        if cmd == 1:
            a, b, c = data[pc + 1:pc + 4]
            data[c] = self.read(data, a, m0) + self.read(data, b, m1)
            self.pc += 4
        elif cmd == 2:
            a, b, c = data[pc + 1:pc + 4]
            data[c] = self.read(data, a, m0) * self.read(data, b, m1)
            self.pc += 4
        elif cmd == 3:
            if self.stdin:
                a = data[pc + 1]
                data[a] = self.stdin.popleft()
                self.pc += 2
            else:
                self.state = 'waiting for input'
        elif cmd == 4:
            a = data[pc + 1]
            self.stdout.append(self.read(data, a, m0))
            self.pc += 2
        elif cmd == 5:
            a, b, *_ = data[pc + 1:]
            if self.read(data, a, m0):
                self.pc = self.read(data, b, m1)
            else:
                self.pc += 3
        elif cmd == 6:
            a, b, *_ = data[pc + 1:]
            if not self.read(data, a, m0):
                self.pc = self.read(data, b, m1)
            else:
                self.pc += 3
        elif cmd == 7:
            a, b, c, *_ = data[pc + 1:]
            data[c] = self.read(data, a, m0) < self.read(data, b, m1)
            self.pc += 4
        elif cmd == 8:
            a, b, c, *_ = data[pc + 1:]
            data[c] = self.read(data, a, m0) == self.read(data, b, m1)
            self.pc += 4
        elif cmd == 99:
            self.state = 'halted'
        else:
            assert False, f'pc={pc}, cmd={cmd}'


thrusts = []
for phases in permutations('56789'):
    amps = [IntCodeComputer(data[:], deque([int(phase)])) for phase in phases]
    for i in range(len(amps)):
        amps[i].stdout = amps[(i + 1) % len(amps)].stdin
    amps[0].stdin.append(0)

    amp_id = 0
    while any(amp.state != 'halted' for amp in amps):
        amp = amps[amp_id]
        amp.resume()
        amp_id = (amp_id + 1) % len(amps)
    thrusts.append(*amps[-1].stdout)
print(max(thrusts))
