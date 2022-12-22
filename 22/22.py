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


def forward(p, n, di):
    for i in range(n):
        npos = np.add(p, dirs[di])
        #print(f"{di}: {p} -> {npos}")
        if (di == 0 or di == 2):
            if npos[0] >= len(map[npos[1]]) or npos[0] < 0 or map[npos[1]][npos[0]] == " ":
                if dirs[di][0] > 0:
                    for j in range(len(map[npos[1]])):
                        if map[npos[1]][j] != " ":
                            npos[0] = j
                            break
                elif dirs[di][0] < 0:
                    for j in range(len(map[npos[1]]) -1, -1 ,-1):
                        if map[npos[1]][j] != " ":
                            npos[0] = j
                            break
        else:
            if npos[1] >= len(map) or npos[1] < 0 or npos[0] >= len(map[npos[1]]) or map[npos[1]][npos[0]] == " ":
                if dirs[di][1] > 0:
                    for j in range(len(map)):
                        if len(map[j]) > npos[0] and map[j][npos[0]] != " ":
                            npos[1] = j
                            break
                elif dirs[di][1] < 0:
                    for j in range(len(map)-1, -1, -1):
                        if len(map[j]) > npos[0] and map[j][npos[0]] != " ":
                            npos[1] = j
                            break

        if map[npos[1]][npos[0]] == "#":
            return p
        p = npos

    return p

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
    p = forward(p, int(nstr), di)
    di = rotate(di, turn)

print((p[1] + 1) * 1000 + (p[0] + 1) * 4 + di)

