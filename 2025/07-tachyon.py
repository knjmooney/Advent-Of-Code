from collections import defaultdict, deque
import json
from unittest import result
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/7/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.decode()
)

data = data.splitlines()
height = len(data)
splitters = {(i, j) for j, r in enumerate(data) for i, c in enumerate(r) if c == "^"}
start = next((i, j) for j, r in enumerate(data) for i, c in enumerate(r) if c == "S")

to_visit = deque([start])
visited = set()
seen = defaultdict(int)
result = 1

while to_visit:
    (i, j) = to_visit.popleft()
    if j + 1 > height:
        continue
    if (i, j) in visited:
        continue
    visited.add((i, j))

    if (i, j) in splitters:
        result += seen[(i, j)] or 1
        to_visit.append((i - 1, j + 1))
        to_visit.append((i + 1, j + 1))
        seen[(i - 1, j + 1)] += seen[(i, j)] or 1
        seen[(i + 1, j + 1)] += seen[(i, j)] or 1
    else:
        to_visit.append((i, j + 1))
        seen[(i, j + 1)] += seen[(i, j)] or 1

print(result)
