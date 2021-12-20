import os
from collections import Counter, namedtuple
from itertools import combinations, product
from parse import parse, findall
dirname = os.path.dirname(__file__)

def rotatex(p):
    a, b, c = p
    return (a, c, -b)

def rotatey(p):
    a, b, c = p
    return (c, b, -a)

def rotatez(p):
    a, b, c = p
    return (b, -a, c)

def all_orientations(p):
    result = []
    for _ in range(2):
        for _ in range(4):
            result.append(p)
            p = rotatex(p)
        p = rotatez(p)
        for _ in range(4):
            result.append(p)
            p = rotatey(p)
        p = rotatez(p)

    pzp = rotatey(p)
    pzm = rotatey(rotatey(pzp))
    for _ in range(4):
        result.append(pzp)
        result.append(pzm)
        pzp = rotatez(pzp)
        pzm = rotatez(pzm)
    return result

def tdiff(x, y):
    return tuple(a - b for a, b in zip(x, y))

def tadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


data = open(f'{dirname}/19-input.txt').read().split('\n\n')
data = [[all_orientations(parse('{:d},{:d},{:d}', l).fixed) for l in d.splitlines()[1:]] for d in data]
N = len(all_orientations((1, 2, 3)))
assert(N == 24)

yet_to_be_scanned = set(range(len(data)))
yet_to_be_scanned.remove(0)
matched_but_not_probed = [(0, 0, (0, 0, 0))]
result = [((0, 0), (0, 0, 0))]
valid_points = set()
while yet_to_be_scanned:
    curr_id, curr_orient, curr_origin = matched_but_not_probed.pop(0)
    curr = data[curr_id]
    for other_id in yet_to_be_scanned.copy():
        for orient in range(N):
            other = data[other_id]
            counts = Counter(tdiff(curr_p[curr_orient], other_p[orient]) for curr_p, other_p in product(curr, other))
            most_common = counts.most_common(1)[0]
            if most_common[1] >= 12:
                relative_to_global_origin = tadd(curr_origin, most_common[0])
                matched_but_not_probed.append((other_id, orient, relative_to_global_origin))
                result.append(((other_id, orient), relative_to_global_origin))
                yet_to_be_scanned.remove(other_id)


for r in result:
    id, orient = r[0]
    for p in data[id]:
        relative_origin = r[1]
        relative_to_global_origin = tadd(p[orient], relative_origin)
        valid_points.add(relative_to_global_origin)

# print(result)
print(len(valid_points))
print(max(sum(abs(e) for e in tdiff(a[1], b[1])) for a in result for b in result))
