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
    print("bad")

hx, hy = 0,0
tx, ty = 0,0
tps = set()

for l in ls:
    d, r = l.split(" ")
    for i in range(int(r)):
        if d == "U":
            hy += 1
        elif d == "D":
            hy -= 1
        elif d == "L":
            hx -= 1
        elif d == "R":
            hx += 1
        else:
            print("bad dir")

        tx, ty = pull(hx, hy, tx, ty)
        tps.add(k(tx,ty))

print(len(tps))

