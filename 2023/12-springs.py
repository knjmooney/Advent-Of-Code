"""
Part 1 was trivial, branch on each '?'. My solution was slow though. ~6 seconds on M1.

Part 2 was harder, it required making the recursion cachable. This meant figuring out
all the different ways I could reduce the string and goal.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import combinations_with_replacement, cycle, chain, repeat, islice, combinations
from math import lcm
import functools

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/12/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

n = 5
data = [d.split() for d in data]
data = [('?'.join(repeat(d, n)), n * tuple(int(f) for f in e.split(','))) for d, e in data]

@functools.cache
def doIt(s, goal):

    result = 0
    s = s.lstrip('.')

    if len(goal) == 0:
        return not '#' in s

    if len(s) == goal[0]:
        return len(goal) == 1 and not '.' in s

    if len(s) < goal[0]:
        return 0

    if s[0] == '#':
        if '.' in s[:goal[0]]:
            return 0

        if s[goal[0]] == '#':
            return 0

        return doIt(s[goal[0] + 1:], goal[1:])
    
    assert s[0] == '?'

    return doIt('.' + s[1:], goal) + doIt('#' + s[1:], goal)

pprint(sum(doIt(a, b) for a, b in data))
