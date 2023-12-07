import json
from requests_cache import CachedSession
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
    match c:
        case (5, ):
            return 10
        case (4, 1):
            return 9
        case (3, 2):
            return 8
        case (3, *_):
            return 7
        case (2, 2, _):
            return 6
        case (2, *_):
            return 5
        case _:
            return 4

def hashIt(input):
    a = input[0]
    b = a.replace('J', '')
    rank = max(handRank(b + ''.join(e)) for e in combinations_with_replacement(cards[1:], 5 - len(b)))
    return (rank, *(cards.index(e) for e in a))

data = sorted(data, key = hashIt)
print(sum(i * int(d[1]) for i, d in enumerate(data, 1)))