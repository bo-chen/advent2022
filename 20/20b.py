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

buf = []
ind = []
i = 0
for l in ls:
    buf.append(int(l) * 811589153)
    ind.append(i)
    i += 1

l = len(buf)

def mixonce(b, ind):
    for oi in range(l):
        i = -1
        for si in range(l):
            if ind[si] == oi:
                i = si
                break

        v = b[i]
        if v == 0:
            continue

        newpos = (v + i) % (l - 1)
        #print(f"i {i} v {v} newpos {newpos} len {l}")
        if newpos < i:
            #print(f"{buf[:newpos]} + {buf[i:i+1]} + {buf[newpos:i]} + {buf[i+1:]}")
            b = b[:newpos] + b[i:i+1] + b[newpos:i] + b[i+1:]
            ind = ind[:newpos] + ind[i:i+1] + ind[newpos:i] + ind[i+1:]
        else: # newpos > i:
            #print(f"{buf[:i]} + {buf[i+1:newpos+1]} + {buf[i:i+1]} + {buf[newpos+1:]}")
            b = b[:i] + b[i+1:newpos+1] + b[i:i+1] + b[newpos+1:]
            ind = ind[:i] + ind[i+1:newpos+1] + ind[i:i+1] + ind[newpos+1:]

        #print(b)

    return b, ind


#print(buf)
#print(done)
for i in range(10):
    buf, ind = mixonce(buf, ind)

for i in range(l):
    if buf[i] == 0:
        print(buf[(i+1000) % l] + buf[(i+2000) % l] + buf[(i+3000) % l])
        break


