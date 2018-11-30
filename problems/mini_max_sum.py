#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min = max = 0
    size = len(arr)
    arr.sort()
    for i in xrange(size-1):
        min += arr[i]
        max += arr[i+1]
    print min, max

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
