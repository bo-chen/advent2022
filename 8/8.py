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

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())

def k(i, j):
    return str(j)+","+str(i)


t = 0
seen = set()
for i in range(len(ls[0])):
    m = -1
    for j in range(len(ls)):
        if int(ls[j][i]) > m:
            m = int(ls[j][i])
            if (k(i,j) not in seen):
                t += 1
                seen.add(k(i,j))

    m = -1
    for j in range(len(ls)-1, -1, -1):
        if int(ls[j][i]) > m:
            m = int(ls[j][i])
            if (k(i,j) not in seen):
                t += 1
                seen.add(k(i,j))

for j in range(len(ls)):
    m = -1
    for i in range(len(ls[0])):
        if int(ls[j][i]) > m:
            m = int(ls[j][i])
            if (k(i,j) not in seen):
                t += 1
                seen.add(k(i,j))

    m = -1
    for i in range(len(ls[0])-1, -1, -1):
        if int(ls[j][i]) > m:
            m = int(ls[j][i])
            if (k(i,j) not in seen):
                t += 1
                seen.add(k(i,j))

print(seen)

for j in range(len(ls)):
    for i in range(len(ls[0])):
        print(k(i,j) + " " + ls[j][i] + " " + str(k(i,j) in seen))

print(t)
