data = [int(d) for d in open('2019/02-input.txt').read().split(',')]
def execute(data, noun, verb):
    data = data[:]
    data[1] = noun
    data[2] = verb
    pc = 0
    while data[pc] != 99:
        cmd, a, b, c = data[pc:pc + 4]
        if cmd == 1:
            data[c] = data[a] + data[b]
        elif cmd == 2:
            data[c] = data[a] * data[b]
        else:
            assert False, data[pc:pc + 4]
        pc += 4
    return data[0]

for noun in range(100):
    for verb in range(100):
        if execute(data, noun, verb) == 19690720:
            print(noun, verb, 100 * noun + verb)