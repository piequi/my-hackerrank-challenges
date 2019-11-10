#!/bin/python

import math
import os
import random
import re
import sys



# Complete the oddNumbers function below.
def oddNumbers(l, r):

    even_numbers = []

    for i in range(l, r+1):
        if i % 2 != 0:
            even_numbers.append(i)

    return even_numbers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input().strip())

    r = int(raw_input().strip())

    res = oddNumbers(l, r)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
