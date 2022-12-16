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
minx = 99999999
maxx = -999999
miny = 9999999
maxy = -9999999

bs = set()

for l in ls:
    ma = re.search("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", l).groups()
    p1 = pktoa(ma[0] + "," + ma[1])
    p2 = pktoa(ma[2] + "," + ma[3])
    d = dist(p1, p2)
    minx = min([p1[0] - d, minx])
    miny = min([p1[1] - d, minx])
    maxx = max([p1[0] + d, maxx])
    maxy = max([p1[1] + d, maxx])

    m[ma[0] + "," + ma[1]] = d
    bs.add(ma[2] + "," + ma[3])

print(minx)
print(maxx)

t = 0
y = 2000000
for x in range(minx, maxx +1):
    c = False
    for k in m:
        if pkey([x, y]) in bs:
            continue
        p1 = pktoa(k)
        if dist(p1, [x, y]) <= m[k]:
            c = True
            break
    if c:
        t += 1

print(t)

