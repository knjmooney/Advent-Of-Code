import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/1/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = [(d[0], int(d[1:])) for d in data.splitlines()]

total = 0
pos = 50
for direction, value in data:
    if direction == "R":
        change = 1
    elif direction == "L":
        change = -1
    for _ in range(value):
        pos += change
        pos %= 100
        if pos == 0:
            total += 1

print(total)