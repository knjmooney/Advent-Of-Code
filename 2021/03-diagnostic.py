from collections import Counter
import re
from pprint import pprint
import os
dirname = os.path.dirname(__file__)

def get_gamma_and_epsilon(data):
    cdata = [Counter(d[i] for d in data) for i in range(len(data[0]))]
    gamma = ''.join((str(int(d['1'] >= d['0']))) for d in cdata)
    epsilon = ''.join((str(int(d['1'] < d['0']))) for d in cdata)
    return (gamma, epsilon)

data = open(f'{dirname}/03-input.txt').read().splitlines()
gamma, epsilon = get_gamma_and_epsilon(data)
print(gamma, epsilon, int(gamma, 2) * int(epsilon, 2) )

oxdata = data[:]
cbdata = data[:]


id = 0
while len(oxdata) > 1:
    gamma, epsilon = get_gamma_and_epsilon(oxdata)
    oxdata = [d for d in oxdata if gamma[id] == d[id]]
    id += 1

id = 0
while len(cbdata) > 1:
    gamma, epsilon = get_gamma_and_epsilon(cbdata)
    cbdata = [d for d in cbdata if epsilon[id] == d[id]]
    id += 1

print(oxdata, cbdata, int(oxdata[0], 2) * int(cbdata[0], 2))
