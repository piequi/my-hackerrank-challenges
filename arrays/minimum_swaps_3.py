#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    sarray = list(arr)
    sarray.sort()
    swaps = 0

    for i in range(len(arr)):
        if arr[i] != sarray[i]:
            for j in range(i+1, len(arr)):
                if arr[j] == sarray[i]:
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp
                    swaps += 1
                    break

    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
