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

root = {"ds":{},"fs":{} }
cur = root
i = 0
while i < len(ls):
    l = ls[i]
    print(l)
    if l == "$ cd /":
        cur = root
        i += 1
        continue
    if l == "$ cd ..":
        cur = cur["p"]
        i += 1
        continue
    if l[:5] == "$ cd ":
        cur = cur["ds"][l[5:]]
        i += 1
        continue
    if l == "$ ls":
        i += 1
        while i < len(ls) and ls[i][0] != "$":
            fz, fn = ls[i].split(" ")
            if fz == "dir":
                cur["ds"][fn] = {"p": cur, "ds":{}, "fs":{}}
            else:
                cur["fs"][fn] = fz
            i += 1

print(root)

def tds(cur):
    if len(cur) == 0:
        return [0,0]
    t = 0
    for s in cur["fs"].values():
        t += int(s)

    tsdt = 0
    for d in cur["ds"].values():
        dz, sdt = tds(d)
        t += dz
        tsdt += sdt

    if t <= 100000:
        tsdt += t
    return [t, tsdt]

print(tds(root))



