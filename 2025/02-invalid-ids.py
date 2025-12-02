import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/2/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = [tuple(int(e) for e in d.split('-')) for d in data.split(',')]

invalid_ids = set()
for i in range(10**5):
    for j in range(2, 11):
        invalid_id = int(str(i) * j)
        if invalid_id > 10**10:
            break
        for d in data:
            if invalid_id >= d[0] and invalid_id <= d[1]:
                invalid_ids.add(invalid_id)
print(sum(invalid_ids))