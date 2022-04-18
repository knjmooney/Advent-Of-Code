#!/usr/bin/python

import numpy as np
import string

from itertools import cycle



data = open("2018/07-input.txt").read().splitlines()
letters = list(string.ascii_uppercase)
N_workers = 5
def time (c): return 60 + ord(c) - ord("A") + 1


# data = open("2018/07-input-test.txt").read().splitlines()
# letters = ["A", "B", "C", "D", "E", "F"]
# N_workers = 2
# def time (c): return 0 + ord(c) - ord("A") + 1


N_let = len(letters)
is_allocated = [False for _ in range(N_let)]
parents = [[] for _ in range(N_let)]

things = [(letter, False, []) for letter in letters]

for line in data:
    par = line[5]
    child = line[-12]

    idx = ord(child) - ord("A")
    parents[idx].append(par)


t = -1
workers = [["", 0] for _ in range(N_workers)]

while any(parents) or any(w[0] for w in workers):
    for w_idx in range(0, N_workers):
        w = workers[w_idx]
        if w[0] and w[1] == 0:
            l = w[0]
            for p_sub in parents:
                if l in p_sub:
                    p_sub.remove(l)
            workers[w_idx][0] = ""

    for idx in range(0, N_let):
        l = letters[idx]
        is_al = is_allocated[idx]
        p = parents[idx]

        if not p and not is_al:
            for w in workers:
                if not(w[0]):
                    w[0] = l
                    w[1] = time(l)
                    is_allocated[idx] = True
                    break


    t += 1
    for w_idx in range(0, N_workers):
        w = workers[w_idx]
        if not(w[1] == 0):
            workers[w_idx][1] -= 1

    line = "{}\t{}\t{}".format(t, workers[0], workers[1]) #  workers[2][0], workers[3][0], workers[4][0]
    print(line)


