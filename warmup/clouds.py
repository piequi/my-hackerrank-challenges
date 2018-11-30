#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    clouds = list(c)
    jumps = 0
    pos = 0

    while pos < (n-2):
        if clouds[pos+1] == 1:
            pos += 2
        elif clouds[pos+2] == 0:
            pos += 2
        else:
            pos += 1
        jumps += 1

    return jumps + (n - pos -1)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(6)

    c = map(int, '0 0 0 1 0 0'.rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()