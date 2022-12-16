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
        ls.append(line.strip())

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

m = {}
minx = 0
maxx = 4000000
#maxx = 20
miny = 0
maxy = 4000000
#maxy = 20

for l in ls:
    ma = re.search("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", l).groups()
    p1 = pktoa(ma[0] + "," + ma[1])
    p2 = pktoa(ma[2] + "," + ma[3])
    d = dist(p1, p2)
    m[ma[0] + "," + ma[1]] = d

for y in range(miny, maxy+1):
    if y % 100000 == 0:
        print(y)
    bb = []
    newm = dict(m)
    for k in m:
        r = m[k]
        p1 = pktoa(k)
        if p1[1] - r > y:
            continue
        if p1[1] + r < y:
            newm.pop(k)
            continue
        dy = abs(p1[1] - y)
        dx = r - dy
        l = p1[0] - dx
        r = p1[0] + dx
        if l < minx and r < minx or l > maxx and r > maxx:
            continue
        bb.append([l , r])

    for b in bb:
        x = b[0] - 1
        if x < minx or x > maxx:
            continue
        c = False
        for bc in bb:
            if x >= bc[0] and x <= bc[1]:
                c = True
                break
        if c == False:
            print(x * 4000000 + y)
            exit(0)
    m = newm

print("bugger")

