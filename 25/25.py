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

sns = []
for l in ls:
    x = list(l)
    x.reverse()
    sns.append(x)

r = []
i = 0
carry = 0
cont = True
while cont:
    cont = False
    acc = carry
    for sn in sns:
        if len(sn) > i:
            cont = True
            if sn[i] == "2":
                acc += 2
            if sn[i] == "1":
                acc += 1
            if sn[i] == "0":
                acc += 0
            if sn[i] == "-":
                acc += -1
            if sn[i] == "=":
                acc += -2

    if acc > 2:
        carry = math.floor((acc + 2) / 5)
        ri = acc - carry * 5
    elif acc < -2:
        carry = math.floor((-1 * acc + 2) / 5)
        ri = acc + carry * 5
        carry = -1 * carry
    else:
        ri = acc
        carry = 0

    if ri == 2:
        ri = "2"
    if ri == 1:
        ri = "1"
    if ri == 0:
        ri = "0"
    if ri == -1:
        ri = "-"
    if ri == -2:
        ri = "="
    r.append(ri)
    i += 1

r.reverse()
print("".join(r))






