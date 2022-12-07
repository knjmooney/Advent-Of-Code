"""
A bit messy, but we got there.
"""

from collections import deque, namedtuple
import json
from pprint import pprint
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/7/input', cookies=json.load(open('cookie.json')))
    .content
    .decode()
    .strip()
    .splitlines()
)

@dataclass
class dir:
    parent:dir = None
    children:list[dir] = field(default_factory=list)
    name:str = None
    size:int = None

root = dir(None, [], None, None)
curdir = root
for line in data:
    if line[0] == '$':
        if line[2:4] == 'cd':
            name = line[5:]
            if name == '..':
                curdir = curdir.parent
                continue
            nextdir = dir(curdir, [], name, None)
            curdir.children.append(nextdir)
            curdir = nextdir            
        else:
            assert line[2:4] == 'ls'
    else:
        size, name = line.split()
        if size == 'dir':
            continue
        curdir.children.append(dir(curdir, None, name, int(size)))

def calculate_sizes(node: dir):
    if node.size is None:
        node.size = sum(calculate_sizes(child) for child in node.children)
    return node.size

def get_sizes(node: dir):
    # If we have children, then we are a directory
    if node.children:
        if node.size <= 100000:
            return node.size + sum(get_sizes(child) for child in node.children)
        else:
            return sum(get_sizes(child) for child in node.children)
    return 0

def find_smallest_suitable_dir(node:dir):
    if node.children:
        if node.size + 70000000 - root.size >= 30000000:
            return min(node.size, min(find_smallest_suitable_dir(child) for child in node.children))
        else:
            return min(find_smallest_suitable_dir(child) for child in node.children)
    return 70000000

calculate_sizes(root)
print(get_sizes(root.children[0]))
print(find_smallest_suitable_dir(root))
    
