#!/bin/python

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    # for 'flat' arr
    #
    # sumR = sumL = 0
    # print len(arr)
    # raw_size = math.sqrt(len(arr))
    # for i in xrange(raw_size):
    #     sumR += arr[i+row_size]
    #     sumL += arr[row_size-i]
    sum = 0
    size = len(arr)

    for i in xrange(size):
        sum += arr[i][i] - arr[i][size-i-1]

    return abs(sum)

if __name__ == '__main__':
    fptr = open('out', 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)
    print result
    fptr.write(str(result) + '\n')

    fptr.close()
