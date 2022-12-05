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

def rank(c):
    if str(c).islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27

t = 0
for i in range(int(len(ls) / 3)):
    e1 = set(ls[i * 3])
    e2 = set(ls[i * 3 + 1])
    e3 = set(ls[i * 3 + 2])

    b = e1.intersection(e2).intersection(e3)
    b = next(iter(b))
    t += rank(b)

print(t)
