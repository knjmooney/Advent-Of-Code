from collections import Counter, namedtuple
import re
from pprint import pprint
import os
from graph import Graph
from parse import parse, findall
dirname = os.path.dirname(__file__)
L = 25
data = [int(s) for s in open(f'{dirname}/09-input.txt').read().splitlines()]
for j in range(len(data)):
    valid_sums = [a+b for i in range(j+1, j+L) for a, b in zip(data[j:j+L], data[i:j+L])]
    if data[j+L] not in valid_sums:
        ans = data[j+L]
        print("Found it", ans)
        break

sums = [(sum(data[:i]), data[i-1]) for i in range(1, len(data) + 1)]
i = 0
while not any(s[0] == ans for s in sums):
    sums = [(s[0] - sums[0][0], s[1]) for s in sums if s[0] - sums[i][0]]

end_value = next(s for s in sums if s[0] == ans)
end_index = sums.index(end_value)
biggest = max(sums[:end_index + 1], key = lambda t : t[1])
smallest = min(sums[:end_index + 1], key = lambda t : t[1])
print(smallest, biggest) 
print(smallest[1] + biggest[1])
