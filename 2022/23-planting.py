from collections import Counter, defaultdict, deque, namedtuple
from functools import cmp_to_key
from itertools import chain, cycle
import json
import os
from pprint import pprint
import re
from requests_cache import CachedSession
from parse import parse
from dataclasses import dataclass, field
import numpy as np
from math import prod
from heapq import heappop, heappush
import functools

dirname = os.path.dirname(__file__)
data = (
    CachedSession()
    .get('https://adventofcode.com/2022/day/23/input', cookies=json.load(open(f'{dirname}/../cookie.json')))
    .content
    .decode()
)