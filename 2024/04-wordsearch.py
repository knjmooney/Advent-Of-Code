'''
2D board with complex numbers and dictionaries.

Complex numbers handle traversing a 2D array.

A dictionary handles the boundary conditions.
'''

from requests_cache import CachedSession
from collections import defaultdict

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/4/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

data = {i + j * 1j: data[i][j] for i in range(len(data)) for j in range(len(data[0]))}

words = []
for k in data:
    for dir in [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]:
        words.append(''.join(data.get(k + i * dir, '') for i in range(4)))

xs = []
for k in data:
    xs.append((
        ''.join(data.get(k + i * (1 + 1j), '') for i in range(-1, 2)),
        ''.join(data.get(k + i * (1 - 1j), '') for i in range(-1, 2))
        ))

print(words.count('XMAS'))
print(sum(x in [('MAS', 'MAS'), ('SAM', 'MAS'), ('MAS', 'SAM'), ('SAM', 'SAM')] for x in xs))
