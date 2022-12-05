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

t = 0
for l in ls:
    h = int(len(l) / 2)
    s1 = set(l[:h])
    s2 = set(l[h:])
    o = next(iter(s1.intersection(s2)))

    if str(o).islower():
        t += ord(o) - ord("a") + 1
    else:
        t += ord(o) - ord("A") + 27

print(t)
