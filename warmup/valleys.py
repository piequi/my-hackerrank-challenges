#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    altitude = 0
    valleys = 0

    for step in s:
        if step == 'U':
            altitude += 1
        elif step == 'D':
            altitude -= 1
        if (altitude == 0 ) and (step == 'U'):
            valleys += 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(8)

    s = "UDDDUDUU"

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()