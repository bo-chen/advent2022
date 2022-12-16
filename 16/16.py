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

print(ns)

def step(tl, cn, opened):
    #print(str(tl),end = "" )
    #print(str(cn),end = "" )
    #print(str(opened),end = "" )
    #print(str(pathed))
    if tl < 0:
        return 0

    bt = 0
    # open
    nopened = set(opened)
    nopened.add(cn)
    tt = ns[cn]["r"] * tl
    tl -= 1

    for nn in ns[cn]["cps"]:
        if nn in nopened:
            continue
        if tl - ns[cn]["cps"][nn] <= 0:
            continue
        t = step(tl - ns[cn]["cps"][nn], nn, nopened)
        if t > bt:
            bt = t

    return bt + tt

print(step(30, "AA", set(["AA"])))
