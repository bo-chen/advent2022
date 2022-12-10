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
nextX = x
clock = 0
nextIns = 0
pc = 0

while pc < len(ls):
    if nextIns == clock:
        ins = ls[pc]
        x = nextX
        if ins == "noop":
            nextIns = clock + 1
        elif ins[:4] == "addx":
            nextX = x + int(ins[5:])
            nextIns = clock + 2
        else:
            print("invalid ins!")
        pc += 1
    if clock % 40 == 0:
        print("")

    if abs(clock % 40 - x) <= 1:
        print("#", end="")
    else:
        print(" ", end="")
    clock += 1

