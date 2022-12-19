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
with open('./t1.txt') as fp:
    for line in fp:
        ls.append(line.strip())

bps = []
maxos = []
for l in ls:
    ms = re.search("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", l).groups()
    bps.append([np.array([int(ms[1]),0,0,0]), np.array([int(ms[2]),0,0,0]),np.array([int(ms[3]),int(ms[4]),0,0]),np.array([int(ms[5]),0,int(ms[6]), 0])])
    maxos.append(max([int(ms[1]), int(ms[2]), int(ms[3])]))

def optbp(bp, robots, res, tl, maxo):
    if tl == 0:
        return res[3], {}

    nres = np.add(res, robots)

    canBuild = [False, False, False, False]
    for br in range(len(bp)):
        rc = bp[br]
        canBuild[br] = np.all(np.greater_equal(res, rc))

    if canBuild[3]:
        nrobots = np.array(robots)
        nrobots[3] += 1
        nnres = np.subtract(nres, bp[3])
        q, nresult = optbp(bp, nrobots, nnres, tl - 1, maxo)
        nresult[33- tl] = ("build geo skip all")
        return q, nresult

    if bp[3][2] <= res[2]:
        q, nresult = optbp(bp, robots, nres, tl - 1, maxo)
        nresult[33-tl] = ("nop waiting on geo")
        return q, nresult

    else:
        best = -1
        bestresult = {}
        if canBuild[2] and robots[2] < bp[3][2]:
            nrobots = np.array(robots)
            nrobots[2] += 1
            nnres = np.subtract(nres, bp[2])
            q, nresult = optbp(bp, nrobots, nnres, tl - 1, maxo)
            '''
            if robots[2] == 0:
                nresult[33-tl] = ("build obs skip due to none")
                return q, nresult

            tto3 = math.ceil(bp[3][2] - res[2]) / robots[2]
            if bp[3][2] > res[2] and tto3 * robots[0] + res[0] >= bp[3][0] + bp[2][0]:
                nresult[33-tl] = ("build obs skip due to enough time")
                return q, nresult
            '''
            if q > best:
                nresult[33-tl] = ("build obs")
                bestresult = nresult
                best = q
        if canBuild[1] and robots[1] < bp[2][1]:
            nrobots = np.array(robots)
            nrobots[1] += 1
            nnres = np.subtract(nres, bp[1])
            q, nresult = optbp(bp, nrobots, nnres, tl - 1, maxo)
            if q > best:
                nresult[33-tl] = ("build clay")
                bestresult = nresult
                best = q
        if canBuild[0] and robots[0] < maxo:
            nrobots = np.array(robots)
            nrobots[0] += 1
            nnres = np.subtract(nres, bp[0])
            q, nresult = optbp(bp, nrobots, nnres, tl - 1, maxo)
            if q > best:
                nresult[33-tl] = ("build ore")
                bestresult = nresult
                best = q
        if nres[0] < 2 * maxo:
            q, nresult = optbp(bp, robots, nres, tl - 1, maxo)
            if q > best:
                nresult[33-tl] = ("nop")
                bestresult = nresult
                best = q

        return best, bestresult

q, result = optbp(bps[0], np.array([1,0,0,0]), np.array([0,0,0,0]), 32, maxos[0])
print(result)
print(q)

'''
t = 0
for i in range(len(bps)):
    bp = bps[i]
    q, result = optbp(bp, np.array([1,0,0,0]), np.array([0,0,0,0]), 32, maxos[i])
    t += q * (i+1)
    print(f'bp {i} q {q}')

print(f"total {t}")
'''
