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


b = 10
ps = []
for i in range(9):
    ps.append([])

for l in ls[:8]:
    for i in range(len(l)):
        if l[i] == "[":
            ps[int(i / 4)].append(l[int(i + 1)])

pm(ps)

def mov(n, f, t):
    ps[t] = ps[f][0:n] + ps[t]
    ps[f] = ps[f][n:]

for l in ls[10:]:
    m = re.match(r"move (\d+) from (\d+) to (\d+)", l)
    n, f, t = m.groups()
    print(int(n),int(f),int(t))
    mov(int(n),int(f) -1,int(t)-1)
    pm(ps)

s = ""
for p in ps:
    s = s + p[0]
print(s)

