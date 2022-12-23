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

elves = set()
j = 0
for l in ls:
    i = 0
    for c in l:
        if c == "#":
            elves.add(pkey([i, j]))
        i += 1


    j += 1


dirs = [[[0,-1],[-1,-1],[1,-1]],[[0,1],[-1,1],[1,1]],[[-1,0],[-1,-1],[-1,1]],[[1,0],[1,-1],[1,1]]]
def moveone(es, ds):
    props = {} # newpos -> oldpos
    for ek in es:
        e = pktoa(ek)
        shouldmove = False
        for j in [-1,0,1]:
            for i in [-1,0,1]:
                if i==0 and j==0:
                    continue
                if pkey(np.add(e, [i,j])) in es:
                    shouldmove = True
                    break
            if shouldmove:
                break
        if shouldmove:
            for d in ds:
                canmove = True
                hasmove = False
                for c in d:
                    cpos = np.add(c, e)
                    if pkey(cpos) in es:
                        canmove = False
                        break
                if canmove:
                    npos = np.add(d[0], e)
                    if pkey(npos) in props:
                        props[pkey(npos)].append(ek)
                    else:
                        props[pkey(npos)] = [ek]
                    hasmove = True
                    break
            if not hasmove:
                props[ek] = [ek]
        else:
            props[ek] = [ek]

    nes = set()
    for pek in props:
        if len(props[pek]) == 1:
            nes.add(pek)
        else:
            for oek in props[pek]:
                nes.add(oek)

    nds = ds[1:] + ds[:1]
    return nes, nds

def cfmm(es):
    xmi = 100
    xma = -100
    ymi = 100
    yma = -100
    for ek in es:
        e = pktoa(ek)
        if e[0] < xmi:
            xmi = e[0]
        if e[0] > xma:
            xma = e[0]
        if e[1] < ymi:
            ymi = e[1]
        if e[1] > yma:
            yma = e[1]

    print(f"[{xmi},{yma}] - [{xma},{yma}]")
    print((xma - xmi + 1) * (yma - ymi + 1))
    '''
    for j in range(ymi, yma +1):
        for i in range(xmi, xma +1):
            if pkey([i,j]) in es:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    '''

    return (xma - xmi + 1) * (yma - ymi + 1)

print(len(elves))
for i in range(100000):
    nelves, dirs = moveone(elves, dirs)
    if nelves == elves:
        print(i + 1)
        exit(0)
    if i % 100 == 0:
        print(i)
        cfmm(elves)
    elves = nelves


print(elves)
print(cfmm(elves) - len(elves))






