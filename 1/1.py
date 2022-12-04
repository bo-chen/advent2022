import math
import numpy as np
import os
import re
import sys
import functools as ft
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

cs = []
c = []
for l in ls:
    if l == "":
        cs.append(c)
        c = []
        continue
    c.append(int(l))
cs.append(c)


ts = []
for c in cs:
    ts.append(ft.reduce(operator.add, c, 0))

ts.sort()
print(ts[-1] + ts[-2] + ts[-3])
