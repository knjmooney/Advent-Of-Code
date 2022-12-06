from collections import deque
import json
from requests_cache import CachedSession
from parse import parse

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/6/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
)

for i in range(len(data)):
    if len(set(data[i:i+14])) == 14:
        print(i+14)
        break
