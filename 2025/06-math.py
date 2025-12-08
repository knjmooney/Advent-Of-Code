import json
from unittest import result
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2025/day/6/input",
        cookies=json.load(open("cookie.json")),
    )
    .content
    .decode()
)

data = data.splitlines()

#transpose data
data = list(map(''.join, zip(*data)))
data = [''] + data

nums = []
result = 0
op = None
while data:
    d = data.pop()
    print(d)
    if d.strip() == '':
        assert op != None
        print(op, nums, int(eval(op.join(nums))))
        result += int(eval(op.join(nums)))
        nums = []
        continue

    if '*' in d:
        op = '*'
        d = d.replace('*', '')
    elif '+' in d:
        op = '+'
        d = d.replace('+', '')
    nums.append(d)

print(result)