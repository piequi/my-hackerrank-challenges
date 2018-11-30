#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    cur = 0
    for i in range(len(arr)):
        # if the value is not correct
        if arr[cur] != cur + 1:
            # find the index of the wrong value
            correct_index = arr[cur] - 1
            # remember the value at that index
            tmp = arr[correct_index]
            # place the wrong value where it should
            arr[correct_index] = arr[cur]
            # store the swapped value
            arr[cur] = tmp
            # count one swap
            swaps += 1
            # move to the correct index of the swapped value
            cur = tmp - 1
        else:
            cur += 1

    return swaps


if __name__ == '__main__':
    fptr = open('swaps.out', 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
