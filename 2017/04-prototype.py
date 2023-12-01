import json
from pprint import pprint
from requests_cache import CachedSession
from collections import Counter, defaultdict
from parse import parse

data = (
    CachedSession()
    .get('https://adventofcode.com/2018/day/4/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", d).fixed for d in sorted(data)]

i = 0
while i < len(data):
    d = data[i]
    parse("Guard {:d} begins shift", d[5]).fixed[0]
    i+=1
    while "Guard" not in data[i][5]:
        i+=1
pprint(data)