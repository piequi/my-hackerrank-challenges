#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    size = len(a)
    for i in range(size, 0, -1):
        for j in range(i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    print('Array is sorted in', swaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[size-1])

    return swaps

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
