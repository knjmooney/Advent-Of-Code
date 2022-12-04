"""
I thought it was a fiddly one. Alana had a much nicer solution that recognised
there were only 9 possible inputs/outcomes and enumerating them all.
"""
import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/2/input', cookies=json.load(open('cookie.json')))
    .content
    .strip()
    .decode()
    .splitlines()
)

data = [d.split() for d in data]

opponent = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

You = {
    'strat1': {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    },
    'wins': {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    },
    'loses': {
        'C': 'A',
        'A': 'B',
        'B': 'C'
    },
    'shape': {
        'A': 1,
        'B': 2,
        'C': 3
    }
}

def score_game1(d):
    opponent_strat = d[0]
    your_strat = You['strat1'][d[1]]
    score = You['shape'][your_strat]
    if opponent_strat == your_strat:
        return score + 3
    if You['wins'][your_strat] == opponent_strat:
        return score + 6
    return score

def score_game2(d):
    opponent_strat = d[0]
    your_strat = d[1]
    if your_strat == 'X':
        shape = You['wins'][opponent_strat]
        return You['shape'][shape]
    if your_strat == 'Y':
        return 3 + You['shape'][opponent_strat]
    shape = You['loses'][opponent_strat]
    return 6 + You['shape'][shape]


data1 = [score_game1(d) for d in data]
print(sum(data1))

data2 = [score_game2(d) for d in data]
print(sum(data2))
