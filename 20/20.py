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
done = []
i = 0
for l in ls:
    buf.append(int(l))
    done.append(False)
    i += 1

i = 0
l = len(buf)
# print(buf)
while True:
    i = i % l
    if np.all(done):
        break
    if done[i]:
        i = (i + 1) % l
        continue

    v = buf[i]
    done[i] = True
    if v == 0:
        i = (i + 1) % l
        continue

    newpos = (v + i) % (l - 1)
    # print(f"i {i} v {v} newpos {newpos} len {l}")
    if newpos < i:
        # print(f"{buf[:newpos]} + {buf[i:i+1]} + {buf[newpos:i]} + {buf[i+1:]}")
        buf = buf[:newpos] + buf[i:i+1] + buf[newpos:i] + buf[i+1:]
        done = done[:newpos] + done[i:i+1] + done[newpos:i] + done[i+1:]
        i = i + 1
    else: # newpos > i:
        # print(f"{buf[:i]} + {buf[i+1:newpos+1]} + {buf[i:i+1]} + {buf[newpos+1:]}")
        buf = buf[:i] + buf[i+1:newpos+1] + buf[i:i+1] + buf[newpos+1:]
        done = done[:i] + done[i+1:newpos+1] + done[i:i+1] + done[newpos+1:]

    #print(buf)
    #print(done)


#print(buf)
#print(done)

for i in range(l):
    if buf[i] == 0:
        print(buf[(i+1000) % l] + buf[(i+2000) % l] + buf[(i+3000) % l])
        break


