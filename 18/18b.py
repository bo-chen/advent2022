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
    return np.array(list(map(lambda x: int(x), pstr.split(","))))

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
    v = pktoa(l)
    if v[0] > maxx:
        maxx = v[0]
        maxv = l

print(np.linalg.norm(np.array([1,0,0])))

walkedf = set()
def walkv(va, na):
    if (pkey(va) + "," + pkey(na)) in walkedf:
        return 0
    walkedf.add(pkey(va) + "," + pkey(na))
    tot = 1

    if na[0] != 0:
        ta = np.array([[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]])
    elif na[1] != 0:
        ta = np.array([[-1,0,0],[1,0,0],[0,0,-1],[0,0,1]])
    else:
        ta = np.array([[-1,0,0],[1,0,0],[0,-1,0],[0,1,0]])

    for t in ta:
        concave = np.add(np.add(va, na), t)
        flat = np.add(va, t)
        negt = np.multiply(-1, t)

        if pkey(concave) in vs:
            tot += walkv(concave, negt)
        elif pkey(flat) in vs:
            tot += walkv(flat, na)
        else:
            tot += walkv(va, t)

    return tot


tot = walkv(pktoa(maxv), [1,0,0])
print(tot)

