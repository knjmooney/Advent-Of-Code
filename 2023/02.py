"""
The hard part was the parsing. I abuse the word "game" to mean multiple things
"""
import json
from requests_cache import CachedSession
from parse import parse

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/2/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)


def parseGame(rawGame):
    return {d[1]: int(d[0]) for g in rawGame.split(", ") if (d := g.split())}


def possibleGame(game):
    result = True
    for g in game:
        red, blue, green = g.get("red", 0), g.get("blue", 0), g.get("green", 0)
        result &= red <= 12 and blue <= 14 and green <= 13
    return result


def minGame(game):
    a, b, c = (
        max(g.get("red", 0) for g in game),
        max(g.get("blue", 0) for g in game),
        max(g.get("green", 0) for g in game),
    )
    return (a * b * c, a, b, c)


data = [parse("Game {:d}: {}", d).fixed for d in data]
data = [(id, [parseGame(d) for d in e.split("; ")]) for id, e in data]
data = [(id, games, possibleGame(games), minGame(games)) for id, games in data]

print(sum(d[0] for d in data if d[2]))
print(sum(d[3][0] for d in data))
