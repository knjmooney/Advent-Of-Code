'''
Tough one for day 1
'''

import json
from requests_cache import CachedSession

data = (
    CachedSession()
    .get(
        "https://adventofcode.com/2023/day/1/input",
        cookies=json.load(open("cookie.json")),
    )
    .content.strip()
    .decode()
    .splitlines()
)

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def mapTo(d):
    if d[0].isdigit():
        return int(d[0])
    for number in numbers.keys():
        if d.startswith(number):
            return numbers[number]
    return None

data = [[e for i in range(len(d)) if (e := mapTo(d[i:]))] for d in data]
data = [10 * d[0] + d[-1] for d in data]
print(sum(data))
