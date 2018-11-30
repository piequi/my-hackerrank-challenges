#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    size = len(arr)
    neg = zer = pos = 0

    for i in xrange(size):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            zer += 1
    print round(float(pos)/size, 6)
    print round(float(neg)/size, 6)
    print round(float(zer)/size, 6)


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
