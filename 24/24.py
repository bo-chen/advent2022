import math
import numpy as np
import os
import re
import sys
import functools
import operator
import heapq

from itertools import count

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


mp = []
for l in ls:
    r = []
    for c in l:
        if c == ".":
            r.append([])
        else:
            r.append([c])
    mp.append(r)


w = len(mp[0])
h = len(mp)

maxt = math.lcm(w-2, h-2)
print(f"w {w} h {h} lcm {maxt}")

openbyt = []
for t in range(maxt):
    openbyt.append(set())
    for j in range(h):
        for i in range(w):
            if mp[j][i] == []:
                openbyt[t].add(pkey([i, j]))
    nm = []
    for j in range(h):
        r = []
        for i in range(w):
            r.append([])
        nm.append(r)
    for j in range(h):
        for i in range(w):
            ss = mp[j][i]
            for s in ss:
                ni = i
                nj = j
                if s == ">":
                    ni = i + 1
                    if ni == w - 1:
                        ni = 1
                elif s == "<":
                    ni = i - 1
                    if ni == 0:
                        ni = w - 2
                elif s == "v":
                    nj = j + 1
                    if nj == h - 1:
                        nj = 1
                elif s == "^":
                    nj = j - 1
                    if nj == 0:
                        nj = h - 2
                nm[nj][ni].append(s)
    mp = nm

print("finished caching openings")

def findp(t0, i0, j0, ig, jg):
    pq = []
    visited = set()
    visited.add(pkey([t0 % maxt, i0, j0]))

    heapq.heappush(pq, [0, t0, i0, j0])
    while True:
        heu, t, i, j = heapq.heappop(pq)
        npos = [i, j]
        if i == ig and j == jg:
            return t
        for d in [[0,0],[1,0],[-1,0],[0,1],[0,-1]]:
            ni = i+d[0]
            nj = j+d[1]
            wrappedt =(t+1) % maxt
            vk =pkey([wrappedt,ni,nj])
            if vk in visited:
                continue
            visited.add(vk)
            if pkey([ni, nj]) in openbyt[wrappedt]:
                dist = abs(ig - ni) + abs(jg - nj)
                heapq.heappush(pq, [t + 1 + dist, t + 1, ni, nj])

t1 = findp(0, 1, 0, w-2, h-1)
print(t1)
t2 = findp(t1, w - 2, h-1, 1, 0)
print(t2)
t3 = findp(t2, 1, 0, w-2, h-1)
print(t3)
