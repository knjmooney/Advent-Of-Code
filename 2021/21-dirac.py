import os
from collections import Counter, namedtuple
dirname = os.path.dirname(__file__)

probs = Counter()
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            probs[i + j + k] += 1

def update(config, factor):
    result = Counter()
    for dice, count in probs.items():
        score0, pos0, score1, pos1, turn = config
        pos0 = (pos0 + dice - 1) % 10 + 1
        score0 += pos0
        result[(score1, pos1, score0, pos0, (turn + 1) % 2)] += factor * count
    return result

configurations = Counter({(0, 7, 0, 9, 0) : 1})
updated = True
while updated:
    updated = False
    new_config = Counter()
    for config, factor in configurations.items():
        if config[0] < 21 and config[2] < 21:
            new_config += update(config, factor)
            updated = True
        else:
            new_config[config] += factor
    configurations = new_config

print(sum([score for config, score in configurations.items() if config[2] > config[0] and config[4] == 0]))
print(sum([score for config, score in configurations.items() if config[2] > config[0] and config[4] == 1]))
