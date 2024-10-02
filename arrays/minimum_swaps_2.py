#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     swaps = 0
#     for i in xrange(len(arr)):
#         if arr[i] != i+1:
#             for j in xrange(i+1, len(arr)):
#                 if arr[j] == i+1:
#                     tmp = arr[j]
#                     arr[j] = arr[i]
#                     arr[i] = tmp
#                     swaps += 1
#                     break
#
#     return swaps

def minimumSwaps(arr) -> int:
    swaps: int = 0
    index: int = 0
    while index < len(arr):
        if arr[index] != index + 1:
            next_value: int = arr[index]
            arr[index], arr[next_value - 1] = arr[next_value - 1], arr[index]
            swaps += 1
        else:
            index += 1

    return swaps



if __name__ == '__main__':
    fptr = open('swaps.out', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
