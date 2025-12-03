import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/3/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

data = data.splitlines()

answer = 0
for line in data:
    result = ''
    for i in reversed(range(12)):
        this_result = max(line[:-i] if i else line)
        line = line[line.index(this_result)+1:]
        result += this_result
    answer += int(result)
print(answer)