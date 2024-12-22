'''
I very much struggled to think about this one. I didn't realise that each level
would reset to A when it pressed the button in the lower layer. There is a
much simpler solution.
'''

from requests_cache import CachedSession
from collections import defaultdict
from heapq import heappop, heappush
from functools import cache

import json
import re

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2024/day/21/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
)

nums = '''\
789
456
123
 0A'''
nums = {(i, j): e for i, r in enumerate(nums.splitlines()) for j, e in enumerate(r) if e != ' '}

arrows = '''\
 ^A
<v>'''
arrows = {(i, j): e for i, r in enumerate(arrows.splitlines()) for j, e in enumerate(r) if e != ' '}


def get_path(src, dst, cont):
    psrc = list(cont.keys())[list(cont.values()).index(src)]
    pdst = list(cont.keys())[list(cont.values()).index(dst)]
    result = []

    if src == dst:
        return [['A']]
    
    i = pdst[0] - psrc[0]
    if i > 0 and (psrc[0] + 1, psrc[1]) in cont:
        results = get_path(cont[(psrc[0] + 1, psrc[1])], dst, cont)
        result += [['v'] + r for r in results]
    elif i < 0 and (psrc[0] - 1, psrc[1]) in cont:
        results = get_path(cont[(psrc[0] - 1, psrc[1])], dst, cont)
        result += [['^'] + r for r in results]

    j = pdst[1] - psrc[1]
    if j > 0 and (psrc[0], psrc[1] + 1) in cont:
        results = get_path(cont[(psrc[0], psrc[1] + 1)], dst, cont)
        result += [['>'] + r for r in results]
    elif j < 0 and (psrc[0], psrc[1] - 1) in cont:
        results = get_path(cont[(psrc[0], psrc[1] - 1)], dst, cont)
        result += [['<'] + r for r in results]

    return result

@cache
def nums_path(src, dst):
    return get_path(src, dst, nums)

@cache
def arrows_path(src, dst):
    return get_path(src, dst, arrows)

@cache
def get_arrow2_cost(pos, t, depth):
    if depth == 0:
        return 1

    paths = arrows_path(pos, t)
    results = []
    for target in paths:
        result = 0
        pos = 'A'
        for t in target:
            result += get_arrow2_cost(pos, t, depth - 1)
            pos = t
        results.append(result)

    return min(results)

def get_arrow_cost(target):
    pos = 'A'
    result = 0
    for t in target:
        cost = get_arrow2_cost(pos, t, 25)
        pos = t
        result += cost
    return result

def get_cost(target):
    pos = 'A'
    result = [[]]
    for t in target:
        results = nums_path(pos, t)
        pos = t
        result = [r + p for r in result for p in results]
    
    return min(get_arrow_cost(tuple(path)) for path in result)

print(sum(get_cost(d) * int(d[:-1]) for d in data.splitlines()))