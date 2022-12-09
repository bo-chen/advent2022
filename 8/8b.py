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

def look(curi, curj):
    t = 1
    th = int(ls[curj][curi])
    d = 0
    for i in range(curi+1,len(ls[0])):
        d += 1
        if int(ls[curj][i]) >= th:
            break

    t = t * d
    d = 0
    for i in range(curi-1,-1,-1):
        d += 1
        if int(ls[curj][i]) >= th:
            break
    t = t * d
    d = 0
    for j in range(curj+1,len(ls)):
        d += 1
        if int(ls[j][curi]) >= th:
            break
    t = t * d
    d = 0
    for j in range(curj-1,-1,-1):
        d += 1
        if int(ls[j][curi]) >= th:
            break
    t = t * d
    return t

t = 0
for i in range(1, len(ls[0]) -1 ):
    for j in range(1, len(ls) -1):
        s = look(i,j)
        if s > t:
            t = s


print(t)
