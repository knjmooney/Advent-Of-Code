from collections import namedtuple, deque
from distutils.errors import DistutilsClassError
from itertools import combinations, combinations_with_replacement, groupby, permutations, product
from time import sleep
from exceptiongroup import catch
from matplotlib.pyplot import text
from requests_cache import CachedSession
from parse import parse, findall
from pprint import pprint
from heapq import merge
import json
import re

cookies = {
    'session':
    '53616c7465645f5fc81b9fa71b1ab2f491aafa23515353950722cf8a8c60ec912375064ec8b6307d3cb36c776c88c6d23a03cd3'
    'ee66d36b432c993ac1e71ab07'
}

data = (
    CachedSession()
    .get('https://adventofcode.com/2015/day/19/input', cookies=cookies)
    .content
    .strip()
    .decode()
)

# data = """e => H
# e => O
# H => HO
# H => OH
# O => HH

# HOHOHO"""


def print_raw(transforms, medicine):
    for t in transforms:
        print(f"{t['fr']} => {t['to']}")
    print('')
    print(medicine)

def simplify(s):
    return ''.join(molecule_map[e] for e in re.findall('[A-Z][^A-Z]*', s))

    
data = data.replace('e', 'E')
transforms, medicine = data.split('\n\n')

transforms = [{'fr': u[0], 'to': u[1]} for t in transforms.splitlines() if (u := t.split(' => '))]

transforms = [t for t in transforms if 'CR' not in t['to']]

print_raw(transforms, medicine)


molecules = set(t['fr'] for t in transforms)
for t in transforms:
    to = t['to']
    molecules.update(re.findall('[A-Z][^A-Z]*', to))
molecule_map = {m: chr(ord('a') + i) for i, m in enumerate(molecules)}

print(molecule_map)

transforms = [{'fr': simplify(t['fr']), 'to': simplify(t['to'])} for t in transforms]
medicine = simplify(medicine)

print_raw(transforms, medicine)

# ends = set()
# for transform in transforms:
#     fr = transform['fr']
#     to = transform['to']
#     n = len(fr)
#     for i in range(len(start)):
#         if fr == start[i:i + n]:
#             ends.add(start[:i] + to + start[i + n:])

# print('p1 =', len(ends))



# def do_it():
#     next = deque([(0, 'e')])
#     seen = {'e'}
#     while True:
#         steps, start = next.popleft()
#         for transform in transforms:
#             fr = transform['fr']
#             to = transform['to']
#             n = len(fr)
#             for i in range(len(start)):
#                 if fr == start[i:i + n]:
#                     m = start[:i] + to + start[i + n:]
#                     if m == medicine:
#                         print(steps + 1)
#                         return
#                     if m not in seen:
#                         seen.add(m)
#                         next.append((steps + 1, m))

# transform_tos = [t['to'] for t in transforms]

# def make_first_replacement(medicine):
#     for i in range(len(medicine)):
#         transforms_left = transforms[:]
#         for j in range(i + 1, len(medicine)):
#             transforms_left = [t for t in transforms_left if t['to'].startswith(medicine[i:j])]
#             if not transforms_left:
#                 break
#             for t in transforms_left:
#                 if t['to'] == medicine[i:j]:
#                     yield medicine[:i] + t['fr'] + medicine[j:]
#     yield None


# medicine = start
# count = 0
# state = []
# while medicine != 'e':
#     medicine_gen = make_first_replacement(medicine)
#     medicine = next(medicine_gen)
#     while not medicine:
#         count, medicine_gen = state.pop()
#         medicine = next(medicine_gen)

#     state.append((count, medicine_gen))
#     count += 1


# print(count)
#  