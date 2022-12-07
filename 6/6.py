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

l = ls[0]
for i in range(0, int(len(l) - 14)):
    print(l[i:int(i+14)])
    print(set(l[i:int(i+14)]))
    if len(set(l[i:int(i+14)])) == 14:
        print(i+14)
        break
