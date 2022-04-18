from itertools import permutations
from collections import deque
from time import sleep
import os
from pynput import keyboard

input = open('2019/13-input.txt').read()
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
            self.write(c, m2, int(self.read(a, m0) < self.read(b, m1)))
            self.pc += 4
        elif cmd == 8:
            a, b, c = data[pc + 1], data[pc + 2], data[pc + 3]
            self.write(c, m2, int(self.read(a, m0) == self.read(b, m1)))
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

def draw_screen(screen):
    elements = {
        0: ' ',
        1: '|',
        2: '#',
        3: '_',
        4: 'o'
    }
    minx = min(x for x, y in screen)
    miny = min(y for x, y in screen)
    maxx = max(x for x, y in screen)
    maxy = max(y for x, y in screen)
    os.system('clear')
    for j in range(miny, maxy + 1):
        for i in range(minx, maxx + 1):
            print(elements[screen[(i, j)]], end='')
        print()


data[0] = 2
computer = IntCodeComputer(data, deque())
stdout = computer.stdout
screen = {}
while computer.state != 'halted':
    computer.resume()
    while stdout:
        x, y, tile = stdout.popleft(), stdout.popleft(), stdout.popleft()
        if x == -1:
            assert y == 0
            score = tile
        else:
            screen[(x, y)] = tile
    draw_screen(screen)
    paddle_pos = next(k for k, v in screen.items() if v == 3)
    ball_pos = next(k for k, v in screen.items() if v == 4)
    if ball_pos[0] < paddle_pos[0]:
        computer.stdin.append(-1)
    elif ball_pos[0] > paddle_pos[0]:
        computer.stdin.append(1)
    else:
        computer.stdin.append(0)

print(score)

