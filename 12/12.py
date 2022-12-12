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

m = []
i = 0
sp = []
ep = []

for l in ls:
    r = []
    j = 0
    for c in l:
        if c == "S":
            sp = [j, i]
            c = "a"
        if c == "E":
            ep = [j, i]
            c = "z"
        r.append(ord(c) - ord("a"))
        j += 1
    m.append(r)
    i += 1

def sfrom(o):
    q = [[o, 0]]
    visited = set()

    def k(pos):
        return str(pos[0]) + "," + str(pos[1])

    while True:
        cur, cd = q[0]
        q = q[1:]

        if cur[0] == ep[0] and cur[1] == ep[1]:
            return cd
        if cur[0] < 0 or cur[0] >= len(m[0]) or cur[1] < 0 or cur[1] >= len(m) or k(cur) in visited:
            continue
        visited.add(k(cur))

        for d in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx, ny =[cur[0] + d[0], cur[1]+ d[1]]
            if nx < 0 or nx >= len(m[0]) or ny < 0 or ny >= len(m) or  m[cur[1]][cur[0]] < m[ny][nx] - 1:
                continue
            q.append([[nx, ny], cd + 1])

        if len(q) == 0:
            print("stuck")
            break

print(sfrom(sp))

