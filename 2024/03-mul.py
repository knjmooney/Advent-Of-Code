'''

'''

import json
from requests_cache import CachedSession
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/3/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

result = 0
do = True
for i in range(len(data)):
    if do and (m := re.match("^mul\((\d+),(\d+)\)", data[i:])):
        result += int(m.group(1)) * int(m.group(2))
    if re.match("^do\(\)", data[i:]):
        do = True
    if re.match("^don't\(\)", data[i:]):
        do = False

print(result)