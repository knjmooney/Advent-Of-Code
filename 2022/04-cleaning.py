import json
from requests_cache import CachedSession
from parse import parse

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/4/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

def contains(d):
    return (d[0] <= d[2] <= d[1]) or (d[0] <= d[3] <= d[1]) or (d[2] <= d[0] <= d[3]) or (d[2] <= d[1] <= d[3])

data = [parse("{:d}-{:d},{:d}-{:d}", d).fixed for d in data]
data = [contains(d) for d in data]
print(sum(data))