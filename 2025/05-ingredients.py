import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/5/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

ranges, ingredients = data.split('\n\n')

ranges = [(int(d[0]), int(d[1])) for line in ranges.splitlines() if (d := line.split('-'))]

ranges = list(reversed(sorted(ranges)))

result = [ranges.pop()]
while ranges:
    lower = result.pop()
    higher = ranges.pop()
    if lower[1] < higher[0]:
        result.append(lower)
        result.append(higher)
    elif lower[1] <= higher[1]:
        result.append((lower[0], higher[1]))
    else:
        result.append(lower)

count = 0
for a, b in result:
    count += 1 + b - a

print(count)