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

x = 1
clock = 1
nextIns = 1
nextAdd = 0
pc = 0

t = 0
while pc < len(ls) and clock < 221:
    if nextIns == clock:
        ins = ls[pc]
        x += nextAdd
        nextAdd = 0
        if ins == "noop":
            nextIns = clock + 1
            nextAdd = 0
        elif ins[:4] == "addx":
            nextAdd = int(ins[5:])
            nextIns = clock + 2
        pc += 1
    if clock % 40 == 20:
        print(clock * x)
        t += clock * x

    clock += 1

print(t)

