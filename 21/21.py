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

ms = {}
for l in ls:
    ma = re.search("^(\w+): (\d+)$", l)
    if ma:
        n, v = ma.groups()
        ms[n] = {"v": int(v)}
    else:
        n, m1, o, m2 = re.search("^(\w+): (\w+) (.) (\w+)$", l).groups()
        ms[n] = {"m1": m1, "o": o, "m2": m2}

def calc(m):
    if "v" in m:
        return m["v"]

    m1 = calc(ms[m["m1"]])
    m2 = calc(ms[m["m2"]])
    if m["o"] == "+":
        return m1 + m2
    if m["o"] == "-":
        return m1 - m2
    if m["o"] == "*":
        return m1 * m2
    if m["o"] == "/":
        return m1 / m2

    print("bad op")

# returns mc, mh. Where mh is the arm with humn
def findArm(m):
    ml = m["m1"]
    mr = m["m2"]

    ms["humn"]["v"] = 1

    ml1 = calc(ms[ml])
    mr1 = calc(ms[mr])

    ms["humn"]["v"] = 2

    ml2 = calc(ms[ml])
    mr2 = calc(ms[mr])

    if ml1 == ml2:
        return ml, mr
    elif mr1 == mr2:
        return mr, ml

    print("can't find direction")

mc, mh = findArm(ms["root"])
target = int(calc(ms[mc]))

def reversen(mn, tar):
    if mn == "humn":
        return tar
    m = ms[mn]
    if "v" in ms[mn]:
        print("non equal")
        return 0

    m1 = m["m1"]
    m2 = m["m2"]
    o = m["o"]
    mc, mh = findArm(m)
    if o == "+":
        tar = tar - calc(ms[mc])
    if o == "*":
        tar = tar / calc(ms[mc])
        return reversen(mh, tar)
    if o == "-":
        if mc == m1:
            tar = calc(ms[mc]) - tar
        else:
            tar = tar + calc(ms[mc])
    if o == "/":
        if mc == m1:
            tar = calc(ms[mc]) / tar
        else:
            tar = tar * calc(ms[mc])
    return reversen(mh, tar)

print(reversen(mh, target))





