import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict
from parse import parse

data = (
    CachedSession()
    .get('https://adventofcode.com/2018/day/4/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", d).fixed for d in sorted(data)]

guards = defaultdict(Counter)
currentId = None
for _, _, _, _, minute, action in data:
    if 'Guard' in action:
        currentId = parse("Guard #{:d} begins shift", action).fixed[0]
    elif action == 'falls asleep':
        fellAsleep = minute
    elif action == 'wakes up':
        for i in range(fellAsleep, minute):
            guards[currentId][i] += 1
    else:
        assert False

results = [(guard.total(), id, guard.most_common(1)) for id, guard in guards.items()]
results = sorted(results, key=lambda x:x[2][0][1])
print(results[-1][1] * results[-1][2][0][0])