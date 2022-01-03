#!/usr/bin/env python3

from sys import argv
from collections import defaultdict, Counter, deque
from re import match, search
from math import ceil

filename = argv[1] if len(argv) > 1 else '0.in'

cases = []
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        cases.append([int(n) for n in line.split(' ')])

def solve(b, a):
    return ceil((2*a)/b)

for case in cases:
    print(solve(*case))