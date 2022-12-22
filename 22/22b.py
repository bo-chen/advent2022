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

def pktoa(pstr):
    return list(map(lambda x: int(x), pstr.split(",")))

def pkey(p):
    return ",".join(map(lambda x: str(x), p))

ls = []
with open('./in.txt') as fp:
    for line in fp:
        ls.append(line[:-1])


ins = ls[-1].strip()
map = ls[:-2]

dirs = [[1,0],[0,1],[-1,0],[0,-1]]
di = 0

start = [map[0].index("."), 0]

def remap(p, di):
    nx, ny = p
    if p[0] >= 50 and p[0] < 100 and p[1] == -1 and di == 3:
        nx = 0
        ny = 150 + p[0] - 50
        di = 0
    elif p[0] == -1 and p[1] >= 150 and p[1] < 200 and di == 2:
        nx = p[1] - 150 + 50
        ny = 0
        di = 1
    elif p[0] >= 100 and p[0] < 150 and p[1] == -1 and di == 3:
        nx = p[0] - 100
        ny = 199
        di = 3
    elif p[0] >= 0 and p[0] < 50 and p[1] == 200 and di == 1:
        nx = p[0] + 100
        ny = 0
        di = 1
    elif p[0] == 150 and p[1] >= 0 and p[1] < 50 and di == 0:
        nx = 99
        ny = 149 - p[1]
        di = 2
    elif p[0] == 100 and p[1] >= 100 and p[1] < 150 and di == 0:
        nx = 149
        ny = 149 - p[1]
        di = 2
    elif p[0] >= 100 and p[0] < 150 and p[1] == 50 and di == 1:
        nx = 99
        ny = p[0] - 50
        di = 2
    elif p[0] == 100 and p[1] >= 50 and p[1] < 100 and di == 0:
        nx = p[1] + 50
        ny = 49
        di = 3
    elif p[0] >= 50 and p[0] < 100 and p[1] == 150 and di == 1:
        nx = 49
        ny = p[0] + 100
        di = 2
    elif p[0] == 50 and p[1] >= 150 and p[1] < 200 and di == 0:
        nx = p[1] - 100
        ny = 149
        di = 3
    elif p[0] == 49 and p[1] >= 0 and p[1] < 50 and di == 2:
        nx = 0
        ny = 149 - p[1]
        di = 0
    elif p[0] == -1 and p[1] >= 100 and p[1] < 150 and di == 2:
        nx = 50
        ny = 149 - p[1]
        di = 0
    elif p[0] >= 0 and p[0] < 50 and p[1] == 99 and di == 3:
        nx = 50
        ny = p[0] + 50
        di = 0
    elif p[0] == 49 and p[1] >= 50 and p[1] < 100 and di == 2:
        nx = p[1] - 50
        ny = 100
        di = 1


    p = [nx, ny]
    if map[p[1]][p[0]] == " ":
        print("missed remap")
    return p, di

def forward(p, n, di):
    for i in range(n):
        npos = np.add(p, dirs[di])
        npos, ndi = remap(npos, di)

        if map[npos[1]][npos[0]] == "#":
            return p, di
        p = npos
        di = ndi

    return p, di

def rotate(di, turn):
    if turn == "R":
        di = (di + 1) % len(dirs)
    elif turn == "L":
        di = (di - 1) % len(dirs)
    return di

p = start
i = 0
while len(ins) > 0:
    mr = re.search("^(\d+)(\w)(.*)$", ins)
    if not mr:
        turn = None
        nstr = int(ins)
        ins = ""
    else:
        nstr, turn, rest = mr.groups()
        ins = rest
    p, di = forward(p, int(nstr), di)
    di = rotate(di, turn)

print((p[1] + 1) * 1000 + (p[0] + 1) * 4 + di)

'''
for x,y,d in [[50, -1, 3],[99,-1,3],[100,-1,3],[149, -1,3], [150, 0,0], [150, 49,0], [149, 50, 1], [100, 50, 1]]:
    cp = [x, y]
    print(f"{cp}:{d} -> {remap(cp, d)}")

print()

for x,y,d in [[100, 50, 0],[100,99,0],[100,100,0],[100, 149,0], [99, 150,1], [50, 150,1], [50, 150, 0], [50, 199, 0]]:
    cp = [x, y]
    print(f"{cp}:{d} -> {remap(cp, d)}")
'''
