import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/3/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

def score(c : str):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27

data1 = [(d[:len(d)//2], d[len(d)//2:]) for d in data]
data1 = [(set(d[0]) & set(d[1])).pop() for d in data1]
data1 = list(map(score, data1))
print(sum(data1))

data2 = [data[i:i+3] for i in range(0, len(data), 3)]
data2 = [(set(d[0]) & set(d[1]) & set(d[2])).pop() for d in data2]
data2 = [score(d) for d in data2]
print(sum(data2))