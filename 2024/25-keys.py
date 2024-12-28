'''
'''

from requests_cache import CachedSession
from collections import defaultdict, Counter
from heapq import heappop, heappush

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/25/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

datas = '''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''

data = data.split('\n\n')

data = [{(i, j) for i, r in enumerate(d.splitlines()) for j, e in enumerate(r) if e == '#'} for d in data]

# locks = [d for d in data if (0,0) in d]
# keys = [d for d in data if (6,0) in d]

result = 0
for a in data:
    for b in data:
        if not a & b:
            result += 1

print(result // 2)