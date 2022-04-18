#!/usr/bin/python

import numpy as np

from itertools import cycle

data = np.loadtxt("2018/01-input.txt", dtype=int)

# data = [+3, +3, +4, -2, -4]

freq = 0
freqs = set([0])
for d in cycle(data):
    freq += d
    if freq in freqs:
        print(freq)
        break
    else:
        freqs.add(freq)
