data = [d.split(',') for d in open('2019/03-input.txt').read().splitlines()]

# data = [
    # 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
    # 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
# ]

def map_wire(instructions):
    source = (0, 0)
    results = []
    for ins in instructions:
        cmd = ins[0]
        value = int(ins[1:])
        if cmd == 'U':
            j, k = source
            results += [(i, k) for i in range(j + 1, j + value + 1)]
            source = (j + value, k)
        elif cmd == 'D':
            j, k = source
            results += [(i, k) for i in range(j - 1, j - value - 1, -1)]
            source = (j - value, k)
        elif cmd == 'R':
            j, k = source
            results += [(j, i) for i in range(k + 1, k + value + 1)]
            source = (j, k + value)
        elif cmd == 'L':
            j, k = source
            results += [(j, i) for i in range(k - 1, k - value - 1, -1)]
            source = (j, k - value)
        else:
            assert False
    return results


A = map_wire(data[0])
B = map_wire(data[1])

# print(A)
# print(B)
print(set(A) & set(B))
print(2 + min(A.index((i, j)) + B.index((i, j)) for i, j in (set(A) & set(B))))