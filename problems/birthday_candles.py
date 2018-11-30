#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    hicandles = [0, 0]
    for i in range(len(ar)):
        if ar[i] > hicandles[0]:
            hicandles[0] = ar[i]
            hicandles[1] = 1
        elif ar[i] == hicandles[0]:
            hicandles[1] += 1
    print hicandles[1]

if __name__ == '__main__':
    fptr = open('out', 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
