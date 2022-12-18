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

vs = set()
for l in ls:
    vs.add(l)


t = 0
for vk in vs:
    x,y,z = pktoa(vk)
    for xd, yd, zd in [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]:
        if pkey([(x+xd),(y+yd),(z+zd)]) in vs:
            continue
        t += 1

print(t)

