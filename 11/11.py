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
with open('./t1.txt') as fp:
    for line in fp:
        ls.append(line)

def runRound(ms, mis):
    for mind in range(len(ms)):
        m = ms[mind]
        for i in m["is"]:
            ni = m["op"](i)
            ni = int(int(ni) / 3)
            if m["test"](ni):
                ms[m["T"]]["is"].append(ni)
            else:
                ms[m["F"]]["is"].append(ni)
            m["is"] = m["is"][1:]
            mis[mind] += 1

ms = []
i = 0

while i < len(ls):
    i += 1
    m = {"is": list(map(lambda s: int(s.strip()), ls[i][18:].split(",")))}
    i += 1
    operator = ls[i][23]
    operand = ls[i][25:].strip()

    if operator == "+":
        if operand == "old":
            m["op"] = lambda x: x + x
        else:
            m["op"] = lambda x, operand = operand: x + int(operand)
    elif operator == "*":
        if operand == "old":
            m["op"] = lambda x: x * x
        else:
            m["op"] = lambda x, operand = operand: x * int(operand)
    else:
        print("bad operator")
    i += 1
    divisor = int(ls[i][21:])
    m["test"] = lambda x, divisor = divisor: (x % divisor) == 0
    i += 1
    m["T"] = int(ls[i][29:])
    i += 1
    m["F"] = int(ls[i][30:])
    ms.append(m)
    i += 2


mis = []
for i in range(len(ms)):
    mis.append(0)

for i in range(20):
    runRound(ms, mis)

mis.sort()

print(mis[-1] * mis[-2])
