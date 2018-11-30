#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)
    rot_a = []

    for i in range(n):
        circ = i
        if circ + d >= n:
            circ -= n
        rot_a.append(a[circ + d])

    # print rot_a
    return rot_a

if __name__ == '__main__':
    fptr = open('left.out', 'w')

    nd = '5 4'.split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, '1 2 3 4 5'.rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
