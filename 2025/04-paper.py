import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/4/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = {
    (r, c)
    for r, line in enumerate(data.splitlines())
    for c, char in enumerate(line)
    if char == "@"
}

def neighbors(r, c):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        yield r + dr, c + dc

def remove(data):
    return {p for p in data if sum(n in data for n in neighbors(*p)) >= 4}

start = len(data)
old_data = None
while data != old_data:
    old_data = data
    data = remove(data)
print(start - len(data))