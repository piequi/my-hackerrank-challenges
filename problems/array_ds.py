#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):

    rarray = []

    for index in range(len(a)):
        rarray.insert(0, a[index])

    return rarray


if __name__ == '__main__':
    fptr = open('out_array_ds', 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
