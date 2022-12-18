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

maxx = -999999
maxv = ""
vs = set()
for l in ls:
    vs.add(l)
    x,y,z = pktoa(l)
    if x > maxx:
        maxx = x
        maxv = l


walkedf = set()
def walkv(va, na):
    if (pkey(va) + "," + pkey(na)) in walkedf:
        return 0
    walkedf.add(pkey(va) + "," + pkey(na))
    tot = 1

    ta = []
    if na[0] != 0:
        ta = [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
    elif na[1] != 0:
        ta = [[-1,0,0],[1,0,0],[0,0,-1],[0,0,1]]
    else:
        ta = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0]]

    for t in ta:
        concave = [va[0]+na[0]+t[0], va[1]+na[1]+t[1], va[2]+na[2]+t[2]]
        flat = [va[0]+t[0], va[1]+t[1], va[2]+t[2]]
        negt = [t[0] * -1, t[1] * -1, t[2] * -1]

        if pkey(concave) in vs:
            tot += walkv(concave, negt)
        elif pkey(flat) in vs:
            tot += walkv(flat, na)
        else:
            tot += walkv(va, t)

    return tot


tot = walkv(pktoa(maxv), [1,0,0])
print(tot)

