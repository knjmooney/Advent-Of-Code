import re
import os
from collections import Counter, namedtuple
from itertools import combinations, product
from pprint import pprint
from typing import List
from graph import Graph
from parse import parse, findall
from math import prod
from dataclasses import dataclass
from functools import cache
from math import sqrt
dirname = os.path.dirname(__file__)
tiles = open(f'{dirname}/20-test-input.txt').read().split('\n\n')

def rotate_tile_90(tile):
    L = len(tile)
    return [[row[i] for row in tile] for i in reversed(range(L))]

def flip_tile(tile):
    return [list(reversed(row)) for row in tile]

def all_orientations(tile):
    r = []
    for _ in range(2):
        s = []
        for _ in range(4):
            s.append(tile)
            tile = rotate_tile_90(tile)
        r.append(s)
        tile = flip_tile(tile)
    return r

def tile_fits(tile, sol_id, board):
    if sol_id[0] > 0:
        uid = board[sol_id[0] - 1][sol_id[1]]
        up_tile = tiles[uid[0]][uid[1]][uid[2]]
        if tile[0] != up_tile[-1]:
            return False
    if sol_id[1] > 0:
        lid = board[sol_id[0]][sol_id[1] - 1]
        le_tile = tiles[lid[0]][lid[1]][lid[2]]
        return [le_row[-1] for le_row in le_tile] == [row[0] for row in tile]
    return True

def jigsaw2(tile_ids, sol_id, board):
    sol_c = (sol_id // W, sol_id % W)
    if not tile_ids:
        return board

    for tile_id in tile_ids:
        for flip in range(2):
            for rotate in range(4):
                if tile_fits(tiles[tile_id][flip][rotate], sol_c, board):
                    board[sol_c[0]][sol_c[1]] = (tile_id, flip, rotate)
                    solution = jigsaw2(tile_ids - {tile_id}, sol_id + 1, board)
                    if solution:
                        return solution

    return None

tiles = {int(t[0].split(':')[0].split()[1]): all_orientations([list(s) for s in t[1:]]) for tile in tiles if (t := tile.splitlines())}
tile_ids = set(tiles.keys())
W = int(sqrt(len(tile_ids)))

board = [[0 for _ in range(W)] for _ in range(W)]
solution = jigsaw2(tile_ids, 0, board)
print([solution[0][0][0] * solution[0][W - 1][0] * solution[W - 1][0][0] * solution[W - 1][W - 1][0]])

for i in range(W):
    for j in range(W):
        tile = tile_id[i][j]
        for row in tile:

