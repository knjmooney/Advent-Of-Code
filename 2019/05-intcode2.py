data = [int(d) for d in open('2019/05-input.txt').read().split(',')]

def pad(d):
    p = '0' * (5 - len(str(d))) + str(d)
    return map(int, (p[0], p[1], p[2], p[3:]))

def read(data, i, immediate_mode):
    if immediate_mode:
        return i
    else:
        return data[i]

def execute(data, stdin):
    stdout = []
    pc = 0
    while data[pc] != 99:
        m2, m1, m0, cmd = pad(data[pc])
        if cmd == 1:
            a, b, c = data[pc + 1:pc + 4]
            data[c] = read(data, a, m0) + read(data, b, m1)
            pc += 4
        elif cmd == 2:
            a, b, c = data[pc + 1:pc + 4]
            data[c] = read(data, a, m0) * read(data, b, m1)
            pc += 4
        elif cmd == 3:
            a = data[pc + 1]
            data[a] = stdin
            pc += 2
        elif cmd == 4:
            a = data[pc + 1]
            stdout.append(read(data, a, m0))
            pc += 2
        elif cmd == 5:
            a, b, *_ = data[pc + 1:]
            if read(data, a, m0):
                pc = read(data, b, m1)
            else:
                pc += 3
        elif cmd == 6:
            a, b, *_ = data[pc + 1:]
            if not read(data, a, m0):
                pc = read(data, b, m1)
            else:
                pc += 3
        elif cmd == 7:
            a, b, c, *_ = data[pc + 1:]
            data[c] = read(data, a, m0) < read(data, b, m1)
            pc += 4
        elif cmd == 8:
            a, b, c, *_ = data[pc + 1:]
            data[c] = read(data, a, m0) == read(data, b, m1)
            pc += 4
        else:
            assert False, f'pc={pc}, cmd={cmd}'
    return stdout


print(execute(data, 5))
