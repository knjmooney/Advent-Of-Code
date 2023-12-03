"""
I figured that a list would be too slow, so I looked up insertion time
complexity here

  https://wiki.python.org/moin/TimeComplexity

I saw that deque has O(k) rotate, and given k == 7, it seemed like a winner.
Worried I had overthought the problem, I looked up other solutions on AoC, and
it turns out, the most upvoted solution is almost line for line the same, so I
think I lucked out on the optimum solution :)
"""

import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict, deque
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2018/day/9/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

print(data)

lastMarble = 100 * 72061
nPlayers = 428

game = deque([0])
scores = defaultdict(int)
for i in range(1, 1 + lastMarble):
    if i % 23 == 0:
        game.rotate(7)
        scores[i % nPlayers] += i + game.pop()
        game.rotate(-1)
    else:
        game.rotate(-1)
        game.append(i)

print(max(scores.values()))