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

ws = ls[0]
wi = 0

line = [[1,1,1,1]]
plus = [[0,1,0],[1,1,1],[0,1,0]]
corner = [[1,1,1],[0,0,1],[0,0,1]]
vert = [[1],[1],[1],[1]]
sq = [[1,1],[1,1]]

ps = [line,plus,corner,vert,sq]
pi = 0

def addLines(n):
    for i in range(n):
        m.append([0,0,0,0,0,0,0])

m = [[1,1,1,1,1,1,1]]


def testP(p, x, y):
    for j in range(len(p)):
        if y+j < 0:
            return False
        for i in range(len(p[0])):
            if x+i < 0 or x+i >=7:

                return False
            if y+j >= len(m):
                continue
            if p[j][i] == 1 and  m[y+j][i+x] == 1:
                return False


    return True

def anchor(p, x, y):
    for j in range(len(p)):
        if y+j < 0:
            print("missed")
            exit(1)

        while y+j >= len(m):
            addLines(1)

        for i in range(len(p[0])):
            if x+i < 0 or x+i >=7:
                print("in wall")
                exit(1)
            if m[y+j][x+i] == 1 and p[j][i] == 1:
                print("bad Collision")
                exit(1)
            if p[j][i] == 1:
                m[y+j][x+i] = 1

def dropP(p, wi):
    x = 2
    y = len(m) + 3

    while True:
        if ws[wi] == ">":
            d = 1
        else:
            d = -1
        wi += 1
        if wi >= len(ws):
            wi = 0

        if testP(p, x+d, y):
            x += d

        if testP(p, x, y-1):
            y -= 1
        else:
            anchor(p,x,y)
            return wi

repeat = 0
firstH = 0
repeats = set()
repeatstr = ""


i = 0
t = 0
firsti = 0
firstt = 0
deltai = 0
deltalt = 0

while True:
    wi = dropP(ps[pi], wi)
    pi += 1
    if pi >= len(ps):
        pi = 0

    rk = pkey([wi, pi])
    if repeatstr == "":
        if rk in repeats:
            repeatstr = rk
            print("repeat is " + rk)
        else:
            repeats.add(rk)

    else:
        if rk == repeatstr:
            repeat += 1
            if repeat == 1:
                firstt = len(m) - 1 + t
                firsti = i
                print("first " + str(i))
            if repeat == 2:
                lastt = len(m) - 1 + t
                deltai = i - firsti
                deltat = lastt - firstt
                print("second " + str(i))
                i += 1
                break
    i += 1
    if len(m) > 2000:
        t += 1000
        m = m[1000:]

final = 1000000000000

skipcycles = int((final - i) / deltai)
skipi = skipcycles * deltai
skipt = skipcycles * deltat

print("skipi " + str(skipi))

t += skipt
i += skipi
print("after skip " + str(i))

while i < final:
    wi = dropP(ps[pi], wi)
    pi += 1
    if pi >= len(ps):
        pi = 0

    i += 1
    if len(m) > 2000:
        t += 1000
        m = m[1000:]

print(len(m) -1 + t)








