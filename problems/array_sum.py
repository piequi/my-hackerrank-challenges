#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum = 0
    for values in ar:
        sum += values
    return sum


if __name__ == '__main__':
    fptr = open('out', 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
