from itertools import permutations
from collections import deque
from pprint import pprint

data = list(open('2019/08-input.txt').read().strip())
W=25
H=6
WH = W * H
T=len(data)

data = [[''.join(data[i:i + WH][j:j + W]) for j in range(0, WH, W)] for i in range(0, T, WH)]
zero_counts = [sum(row.count('0') for row in layer) for layer in data]
min_zero_count = min(zero_counts)
min_zero_count_layer = data[zero_counts.index(min_zero_count)]
one_count = sum(row.count('1') for row in min_zero_count_layer)
two_count = sum(row.count('2') for row in min_zero_count_layer)
pprint(one_count * two_count)

final_image = [['2'] * len(row) for row in data[0]]
for layer in data:
    for i in range(H):
        for j in range(W):
            if final_image[i][j] == '2':
                final_image[i][j] = layer[i][j]

final_image = [['#' if e == '1' else ' ' for e in row] for row in final_image]
print('\n'.join(''.join(row) for row in final_image))
