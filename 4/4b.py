import math
import numpy as np
import os
import re
import sys

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

pairs = []
with open('./input.txt') as fp:
    for line in fp:
        if len(line.strip()) == 0:
            break
        [r1, r2] = line.strip().split(",")
        [r1s, r1e] = map(int, r1.split("-"))
        [r2s, r2e] = map(int, r2.split("-"))
        pairs.append({"p1":[r1s, r1e],"p2":[r2s,r2e] })

def overlap(r1, r2):
    return not(r1[0] > r2[1] or r1[1] < r2[0])

ts = 0
for p in pairs:
    if overlap(p["p1"],p["p2"]) or overlap(p["p2"],p["p1"]):
        ts += 1


print(ts)


