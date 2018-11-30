#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    for i in xrange(len(arr)):
        if arr[i] != i+1:
            for j in xrange(i+1, len(arr)):
                if arr[j] == i+1:
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp
                    swaps += 1
                    break

    return swaps


if __name__ == '__main__':
    fptr = open('swaps.out', 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)
    print res
    fptr.write(str(res) + '\n')

    fptr.close()
