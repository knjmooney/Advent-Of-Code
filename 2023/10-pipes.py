"""
Part 1 is straightforward, tedious programming of the rules, and then you just
have to figure out what starting direction would work.

Part 2 is more interesting. We have the bounds from part 1, so we walk around
the loop and look either left or right, depending on whether the loop is
clockwise or anti-clockwise. I think I've hardcoded anti-clockwise.
"""

import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import combinations_with_replacement, cycle, chain, repeat, islice
from math import lcm

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/10/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)


def tadd(a, b):
    return tuple(e + f for e, f in zip(a, b))


def doTurn(p, currDir):
    v = grid[p]
    return (currDir + changes[currDir].index(v) - 1) % len(dirs)


def straight(p, currDir):
    return tadd(p, moves[currDir])


def getLoop(dir):
    node = straight(start, dir)
    locs = {start}

    while node != start:
        locs.add(node)
        dir = doTurn(node, dir)
        node = straight(node, dir)

    return locs


def getAllNotInBounds(p, dir):
    p = straight(p, dir)
    result = {p}
    while p not in bounds:
        if p not in grid:
            raise "Wrong orientation"
        result.add(p)
        p = straight(p, dir)
    return result


def getEnclosed(dir, turn):
    node = straight(start, dir)

    enclosed = set()
    while node != start:
        locs.add(node)
        enclosed.update(getAllNotInBounds(node, (dir + turn) % len(dirs)))
        dir = doTurn(node, dir)
        enclosed.update(getAllNotInBounds(node, (dir + turn) % len(dirs)))
        node = straight(node, dir)

    return enclosed


grid = {(i, j): e for i, row in enumerate(data) for j, e in enumerate(row)}
start = next(k for k, v in grid.items() if v == "S")

dirs = "DRUL"
changes = ["J|L", "7-J", "F|7", "L-F"]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

loops = []
for dir in range(len(dirs)):
    try:
        loops.append((getLoop(dir), dir))
    except:
        pass

assert len(loops) == 2
assert not (loops[0][0] ^ loops[1][0])

locs, dir = loops[0]
print("Part 1:", len(locs) // 2)

bounds = set(locs)

# Orientation matters, the 1 means anticlockwise, -1 means clockwise. Somehow
# the boundary ended up in the result, so need to delete it again.
try:
    enclosed = getEnclosed(dir, 1) - bounds
    print("Part 2:", len(enclosed))
except:
    pass
try:
    enclosed = getEnclosed(dir, -1) - bounds
    print("Part 2:", len(enclosed))
except:
    pass
