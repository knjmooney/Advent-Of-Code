"""

"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/4/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = [parse("Card {:3d}: {} | {}", d).fixed for d in data]
data = [(d[1].split(), d[2].split()) for d in data]

scores = [len(set(d[0]) & set(d[1])) for d in data]

result = [1] * len(data)
for i, score in enumerate(scores):
    for j in range(i + 1, min(len(data), i + 1 + score)):
        result[j] += result[i]

print(sum(result))
