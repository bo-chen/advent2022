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

i = 0
pairi = 1

s = 0

def isRightOrder(l, r):
    if type(l) is list and type(r) is int:
        r = [r]
    if type(l) is int and type(r) is list:
        l = [l]

    if type(l) is int:
        if l == r:
            return -1
        if l < r:
            return 1
        else:
            return 0

    if type(l) is list:
        for i in range(len(l)):
            if i >= len(r):
                return 0
            ret = isRightOrder(l[i], r[i])
            if ret >= 0:
                return ret

        if len(l) < len(r):
            return 1

    return -1


while i < len(ls):
    left = json.loads(ls[i])
    right = json.loads(ls[i+1])
    ret = isRightOrder(left, right)
    if ret == 1:
        s += pairi
    elif ret == -1:
        print("whole pair same")

    i += 3
    pairi += 1

print(s)
