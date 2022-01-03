#!/usr/bin/env python3

from sys import argv
from collections import defaultdict, Counter, deque
from re import match, search

filename = argv[1] if len(argv) > 1 else '0.in'
N = -1
cases =[]
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if i == 0:
            N = int(line)
        else:
            cases.append([int(n) for n in line.split(' ')])

def reflectPoint(px, py, qx, qy):
    return 2*qx-px, 2*qy-py

for case in cases:
    print(' '.join([str(n) for n in reflectPoint(*case)]))