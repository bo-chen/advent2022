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

bps = []
maxos = []
for l in ls:
    ms = re.search("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", l).groups()
    bps.append([np.array([int(ms[1]),0,0,0]), np.array([int(ms[2]),0,0,0]),np.array([int(ms[3]),int(ms[4]),0,0]),np.array([int(ms[5]),0,int(ms[6]), 0])])
    maxos.append(max([int(ms[1]), int(ms[2]), int(ms[3])]))

itos = {0: "ore", 1:"clay", 2:"obs", 3:"geo"}
tott = 32

def optbp(bp, robots, res, tl, maxo):
    if tl <= 0:
        return res[3], {}

    bestq = 0
    bestRes = {}
    for ri in range(len(bp) - 1, -1, -1):
        if ri == 0 and robots[0] >= maxo:
            continue
        if ri == 1 and robots[1] >= bp[2][1]:
            continue
        if ri == 2 and robots[2] >= bp[3][2]:
            continue
        robotcost = bp[ri]
        maxT = 0
        for i in range(len(res)):
            rc = robotcost[i]
            if rc == 0:
                continue
            if robots[i] == 0:
                maxT = -1
                break
            if rc < res[i]:
                continue
            ttf = math.ceil((rc - res[i]) / robots[i])
            if maxT < ttf:
                maxT = ttf

        if maxT < 0 or maxT >= tl:
            continue
        nrobots = np.array(robots)
        nrobots[ri] += 1
        nres = np.add(res, np.multiply(maxT + 1, robots))
        nres = np.subtract(nres, robotcost)
        q, result = optbp(bp, nrobots, nres, tl - 1 - maxT, maxo)
        if q > bestq:
            bestq = q
            result[tott + 1 - tl + maxT] = f"build {itos[ri]}"
            bestRes = result

    q = robots[3] * tl + res[3]
    if q >= bestq:
        return q, {(tott + 1 - tl): f"nop rest for {q}"}

    return bestq, bestRes

# q, result = optbp(bps[0], np.array([1,0,0,0]), np.array([0,0,0,0]), tott, maxos[0])
# print(result)
# print(q)

t = 1
for i in range(3):
    bp = bps[i]
    q, result = optbp(bp, np.array([1,0,0,0]), np.array([0,0,0,0]), tott, maxos[i])
    t *= q
    print(f"{i} done")

print(f"total {t}")
