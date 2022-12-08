from collections import deque, namedtuple
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/8/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

assert len(data) == len(data[0])
data = np.array([np.array([int(t) for t in d]) for d in data])

def is_visible(i, j):
    if i == 0 or j == 0 or i == len(data) - 1 or j == len(data) - 1:
        return True 
    return (
        max(data[0:i, j]) < data[i, j] or
        max(data[i+1:, j]) < data[i, j] or
        max(data[i, 0:j]) < data[i, j] or
        max(data[i, j+1:]) < data[i, j]        
    )

visible_trees = [is_visible(i, j) for i in range(len(data)) for j in range(len(data))]
print(sum(t for t in visible_trees))

def until_bigger(e, arr):
    for i, d in enumerate(arr):
        if e <= d:
            return i + 1
    return i + 1

def inner_visible_trees(i, j):
    B = len(data) - 1
    e = data[i, j]
    le = 0 if i == 0 else until_bigger(e, reversed(data[0:i, j]))
    ri = 0 if i == B else until_bigger(e, data[i+1:, j])
    up = 0 if j == 0 else until_bigger(e, reversed(data[i, :j]))
    do = 0 if j == B else until_bigger(e, data[i, j+1:])

    return le * ri * up * do

inner_visible_trees = [inner_visible_trees(i, j) for i in range(len(data)) for j in range(len(data))]
print(max(t for t in inner_visible_trees))
