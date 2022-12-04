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

def winscore(o, y):
    if o == "A" and y == "X" or o =="B" and y=="Y" or o == "C" and y == "Z":
        return 3
    if o=="A" and y =="Y" or o=="B" and y=="Z" or o == "C" and y=="X":
        return 6
    return 0

def sscore(y):
    if y == "X":
        return 1
    if y == "Y":
        return 2
    if y == "Z":
        return 3

ts = 0
for l in ls:
    o, y = l.split(" ")
    ts += winscore(o, y) + sscore(y)

print(ts)

