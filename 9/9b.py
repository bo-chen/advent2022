import math
import numpy as np
import os
import re
import sys
import functools
import operator

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())


def k(x,y):
    return str(x) + "," + str(y)

def pull(hx, hy, tx, ty):
    dx = hx - tx
    dy = hy - ty
    td = abs(dx) + abs(dy)
    if td <= 1:
        return tx, ty
    if td == 2:
        if abs(dx) == 2:
            return int(dx / 2) + tx, ty
        elif abs(dy) == 2:
            return tx, int(dy / 2) + ty
        return tx, ty
    if td == 3:
        if abs(dx) == 2:
            return int(dx / 2) + tx, hy
        elif abs(dy) == 2:
            return hx, int(dy / 2) + ty
    if td == 4:
        return int(dx / 2) + tx, int(dy / 2) + ty
    print("bad")


ts = []
for i in range(10):
    ts.append([0,0])

tps = set()
for l in ls:
    d, r = l.split(" ")

    for i in range(int(r)):
        if d == "U":
            ts[0][1] += 1
        elif d == "D":
            ts[0][1] -= 1
        elif d == "L":
            ts[0][0] -= 1
        elif d == "R":
            ts[0][0] += 1
        else:
            print("bad dir")

        for i in range(1,10):
            ts[i][0], ts[i][1] = pull(ts[i-1][0], ts[i-1][1], ts[i][0], ts[i][1])
        tps.add(k(ts[9][0],ts[9][1]))

print(len(tps))

