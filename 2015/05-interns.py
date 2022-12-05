r"""
Alternatively, this can be solved with backreferences

From reddit:

    > cat input |  grep "\(..\).*\1" | grep "\(.\).\1" | wc -l

"""

from collections import namedtuple
from time import sleep
from requests_cache import CachedSession
from parse import parse
from pprint import pprint

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/5/input', cookies=cookies)
    .content
    .decode()
    .splitlines()
)

def count_vowels(s: str):
    return sum(s.count(v) for v in 'aeiou')

def has_double_letter(s: str):
    return any(d == e for d, e in zip(s, s[1:]))

def has_bad_string(s: str):
    return any(d in s for d in ['ab', 'cd', 'pq', 'xy'])

def is_nice_p1(s: str):
    return count_vowels(s) >= 3 and has_double_letter(s) and not has_bad_string(s)

def has_double_letter_split(s: str):
    return any(d == e for d, e in zip(s, s[2:]))

def has_double_pair(s: str):
    if len(s) == 3:
        return False
    if s[:2] in s[2:]:
        return True
    return has_double_pair(s[1:])


data = [d for d in data if has_double_letter_split(d) and has_double_pair(d)]

print(len(data))
