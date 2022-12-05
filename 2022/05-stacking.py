from collections import deque
import json
from requests_cache import CachedSession
from parse import parse

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/5/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
)

stacks_raw, ops_raw = [d.splitlines() for d in data.split('\n\n')]

stacks_raw, stack_nums = stacks_raw[:-1], stacks_raw[-1]

stacks = [[] for i in range((len(stacks_raw[0]) + 1)//4)]
for line in stacks_raw:
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[(i-1)//4].insert(0, line[i])

for op in ops_raw:
    n, frm, to = parse('move {:d} from {:d} to {:d}', op).fixed
    frm = frm - 1
    to = to - 1
    stacks[frm], stacks[to] = stacks[frm][:-n], stacks[to] + stacks[frm][-n:]

result = ''.join(stack[-1] for stack in stacks)
print(result)