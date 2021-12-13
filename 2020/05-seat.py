import re
from pprint import pprint
import os
dirname = os.path.dirname(__file__)

data = open(f'{dirname}/05-input.txt').read().splitlines()
data = [(d, d.replace('F', '1').replace('B', '0').replace('L', '1').replace('R', '0')) for d in data]
data = [(d[0], d[1], 127 - int(d[1][:7], 2), 7 - int(d[1][7:], 2)) for d in data]
data = sorted([d[2] * 8 + d[3] for d in data])
print(max(data))
data = zip(data, data[1:])
print(next((a, b) for a, b in data if a != b-1))