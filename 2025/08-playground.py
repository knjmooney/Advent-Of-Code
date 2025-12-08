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

data = data.splitlines()
data = [(int(a), int(b), int(c)) for a, b, c in (line.split(",") for line in data)]
coords = data
nnodes = len(data)
to_connect = 1000

def dist(a, b):
    return sum((x1 - x2) ** 2 for x1, x2 in zip(a, b))

data = [(dist(data[a], data[b]), a, b) for a, b in combinations(range(len(data)), 2)]
data = sorted(data)

graph = [{i} for i in range(nnodes)]
count = 0
for _, a, b in data:
    if a in graph[b]:
        continue
    graph[a] |= graph[b]
    graph[b] |= graph[a]
    for nn in graph[b]:
        graph[nn] |= graph[b]
    for nn in graph[a]:
        graph[nn] |= graph[b]

    if(len(graph[a])) == nnodes:
        print(coords[a][0] * coords[b][0])
        break
