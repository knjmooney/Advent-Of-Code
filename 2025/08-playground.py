from itertools import combinations
import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/8/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.decode()
)


def dist(a, b):
    return sum((x1 - x2) ** 2 for x1, x2 in zip(a, b))


data = [
    (int(a), int(b), int(c))
    for a, b, c in (line.split(",") for line in data.splitlines())
]
nnodes = len(data)

data = sorted(
    (dist(data[a], data[b]), a, b, data[a], data[b])
    for a, b in combinations(range(len(data)), 2)
)

graph = [{i} for i in range(nnodes)]
for _, a, b, pa, pb in data:
    graph[a] |= graph[b]
    graph[b] = graph[a]
    for nn in graph[b]:
        graph[nn] = graph[b]

    if (len(graph[a])) == nnodes:
        print(pa[0] * pb[0])
        break
