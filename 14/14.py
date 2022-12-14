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
with open('./in.txt') as fp:
    for line in fp:
        ls.append(line.strip())

def ptoxy(pstr):
    xs, ys = pstr.split(",")
    return [int(xs), int(ys)]

def k(p):
    return str(p[0]) + "," + str(p[1])

def sgn(x):
    if x > 0:
        return 1
    return -1

m = {}
maxy = 0
for l in ls:
    ps = l.split(" -> ")
    c = ptoxy(ps[0])
    for p in ps[1:]:
        p = ptoxy(p)
        if c[0] != p[0]:
            for x in range(c[0],p[0], sgn(p[0]-c[0])):
                m[k([x,c[1]])] = "#"

        else:
            for y in range(c[1], p[1], sgn(p[1] - c[1])):
                m[k([c[0],y])] = "#"
                if y > maxy:
                    maxy = y
        c = p
    m[k(c)] = "#"
    if c[1] > maxy:
        maxy = c[1]

print(m)

def dropone(p):
    if not(k([p[0],p[1]+1]) in m.keys()):
        return [p[0], p[1] +1]
    if not(k([p[0]-1,p[1]+1]) in m.keys()):
        return [p[0]-1, p[1] +1]
    if not(k([p[0]+1,p[1]+1]) in m.keys()):
        return [p[0]+1, p[1] +1]

    return "r"

print(maxy)

def dropall():
    p = [500,0]
    r = [500,0]
    while r != "r":
        p = r
        r = dropone(p)
        if p[1] > maxy:
            return True
    m[k(p)] = "o"
    return False

i = 0
while True:
    ret = dropall()
    if ret:
        print(i)
        break
    i += 1
















