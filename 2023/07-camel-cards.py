import json
from requests_cache import CachedSession
from parse import parse
from pprint import pprint
from collections import Counter
from itertools import combinations_with_replacement

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/7/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode().splitlines()
)

data = [(e[0], e[1]) for d in data if (e:=d.split())]

cards = 'J23456789TJQKA'

def handRank(h):
    assert len(h) == 5
    c = tuple(e[1] for e in Counter(h).most_common())
    if c[0] == 5:
        return 10
    elif c[0] == 4:
        return 9
    elif c[0] == 3 and c[1] == 2:
        return 8
    elif c[0] == 3:
        return 7
    elif c[0] == 2 and c[1] == 2:
        return 6
    elif c[0] == 2:
        return 5
    return 4

def hashIt(input):
    a = input[0]
    b = a.replace('J', '')
    rank = max(handRank(b + ''.join(e)) for e in combinations_with_replacement(cards[1:], 5 - len(b)))
    return (rank, *(cards.index(e) for e in a))

data = sorted(data, key = hashIt)
print(list((d, hashIt(d)) for d in data))
print(sum(i * int(d[1]) for i, d in enumerate(data, 1)))