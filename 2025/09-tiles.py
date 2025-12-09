"""
Runtime was 7 minutes until I optimised the walk function.

I also messed up the size calculation by putting the +1 inside the abs:
abs(a-b+1)
"""

from itertools import combinations
import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/9/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.decode()
)


def set_if_empty(grid, i, c):
    grid[i] = grid.get(i, c)


data = data.splitlines()
data = [(int(a), int(b)) for a, b in (line.split(",") for line in data)]
print("start:", data[0], "->", data[1], "->", data[2])

part1 = max(
    (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1])) for a, b in combinations(data, 2)
)

print("Part 1:", part1)

grid = dict()
for a, b in zip(data, data[1:] + [data[0]]):
    if a == b:
        continue
    assert (a[0] != b[0] and a[1] == b[1]) or (a[0] == b[0] and a[1] != b[1])
    dx = -1 if a[0] > b[0] else 1 if a[0] < b[0] else 0
    dy = -1 if a[1] > b[1] else 1 if a[1] < b[1] else 0
    lx = dy
    ly = dx * -1
    grid[a] = "#"
    set_if_empty(grid, (a[0] + lx, a[1] + ly), "O")
    a = (a[0] + dx, a[1] + dy)
    while a != b:
        grid[a] = "X"
        set_if_empty(grid, (a[0] + lx, a[1] + ly), "O")
        a = (a[0] + dx, a[1] + dy)
    grid[a] = "#"
    set_if_empty(grid, (a[0] + lx, a[1] + ly), "O")

outside_row = [list() for _ in range(100000)]
outside_col = [list() for _ in range(100000)]
for key, value in grid.items():
    if grid[key] == "O":
        outside_row[key[1]].append(key[0])
        outside_col[key[0]].append(key[1])


def walk(a, b):
    for o in outside_row[a[1]]:
        if min(a[0], b[0]) < o < max(a[0], b[0]):
            return False
    for o in outside_col[a[0]]:
        if min(a[1], b[1]) < o < max(a[1], b[1]):
            return False
    return True


result = 0
todo = reversed(
    sorted(
        ((1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1])), a, b)
        for a, b in combinations(data, 2)
    )
)
for size, a, b in todo:
    if not walk(a, (b[0], a[1])):
        continue
    if not walk((b[0], a[1]), b):
        continue
    if not walk(b, (a[0], b[1])):
        continue
    if not walk((a[0], b[1]), a):
        continue
    result = max(result, size)
    print("FOUND:", result, a, b, size)
    break
