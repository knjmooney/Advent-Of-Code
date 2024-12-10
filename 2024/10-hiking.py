'''
I somehow solved them in reverse, part 2 was easier than part 1.
'''

from requests_cache import CachedSession
from collections import defaultdict

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/10/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = {i + j * 1j: int(data[i][j]) if data[i][j] != '.' else -1 for i in range(len(data)) for j in range(len(data[0]))}

def walk(path: list):
    result = []
    p = path[-1]
    
    if data[p] == 9:
        return [p]

    dir = -1
    for i in range(4):
        dir *= 1j
        nextp = p + dir
        if data.get(nextp, 0) == data[p] + 1:
            result += walk(path + [nextp])

    return result


print(sum([len(set(walk([p]))) for p in data if data[p] == 0]))
print(sum([len(walk([p])) for p in data if data[p] == 0]))