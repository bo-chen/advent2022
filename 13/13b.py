import math
import numpy as np
import os
import re
import sys
import functools
import operator
import json

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

def isRightOrder(l, r):
    if type(l) is list and type(r) is int:
        r = [r]
    if type(l) is int and type(r) is list:
        l = [l]

    if type(l) is int:
        if l == r:
            return 0
        if l < r:
            return -1
        else:
            return 1

    if type(l) is list:
        for i in range(len(l)):
            if i >= len(r):
                return 1
            ret = isRightOrder(l[i], r[i])
            if ret != 0:
                return ret

        if len(l) < len(r):
            return -1

    return 0

avs = [[[2]],[[6]]]
for l in ls:
    if len(l) > 0:
        avs.append(json.loads(l))

kf = functools.cmp_to_key(isRightOrder)
savs = sorted(avs, key=kf)
fi = savs.index([[2]])
li = savs.index([[6]])

print((fi + 1) * (li + 1))
