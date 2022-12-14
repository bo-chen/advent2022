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

m = {}
maxy = 0
for l in ls:
    ps = l.split(" -> ")
    c = pktoa(ps[0])
    for p in ps[1:]:
        p = pktoa(p)
        if c[0] != p[0]:
            for x in range(c[0], p[0], int(math.copysign(1, p[0] - c[0]))):
                m[pkey([x,c[1]])] = "#"

        else:
            for y in range(c[1], p[1], int(math.copysign(1, p[1] - c[1]))):
                m[pkey([c[0],y])] = "#"
                if y > maxy:
                    maxy = y
        c = p
    m[pkey(c)] = "#"
    if c[1] > maxy:
        maxy = c[1]

maxy += 2

def dropone(p):
    if p[1] + 1 >= maxy:
        return "r"
    for d in [0,-1,1]:
        if not(pkey([p[0] + d,p[1] + 1]) in m.keys()):
            return [p[0] + d, p[1] + 1]

    return "r"

print(maxy)

def dropall():
    p = [500,0]
    r = [500,0]
    while r != "r":
        p = r
        r = dropone(p)
    m[pkey(p)] = "o"
    return p

i = 0
while True:
    ret = dropall()
    i += 1
    if ret == [500,0]:
        print(i)
        break
















