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

ns = {}
for l in ls:
    ma = re.search("^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$", l).groups()
    r = int(ma[1])
    ps  = ma[2].split(", ")
    ns[ma[0]] = {"r": r, "ps": ps}

numn = len(ns)
for n in ns:
    cps = {}
    fs = ns[n]["ps"]
    d = 0
    while len(cps) < numn -1:
        if len(fs) == 0:
            break
        d += 1
        nfs = []
        for nextn in fs:
            if nextn == n:
                continue
            if nextn in cps.keys():
                continue
            cps[nextn] = d
            for pn in ns[nextn]["ps"]:
                if pn not in cps:
                    nfs.append(pn)
        fs = nfs

    fcps = {}
    for fn in cps:
        if ns[fn]["r"] > 0:
            fcps[fn] = cps[fn]
    ns[n]["cps"] = fcps

def step(tl1, tl2, cn1, cn2, togo):
    if tl1 < tl2:
        return step(tl2, tl1, cn2, cn1, togo)

    bt = 0
    avail = False
    for nn in togo:
        if tl1 - ns[cn1]["cps"][nn] <= 0:
            continue
        avail = True
        ntogo = set(togo)
        ntogo.remove(nn)
        ntl = tl1 - ns[cn1]["cps"][nn] - 1
        t = ntl * ns[nn]["r"]
        t += step(tl2, ntl, cn2, nn, ntogo)
        if t > bt:
            bt = t

    if not avail:
        if tl2 <= 1:
            return 0
        return step(tl2, 0, cn2, cn1, togo)


    return bt

togo = ns["AA"]["cps"].keys()
print(step(26, 26, "AA", "AA", togo))
