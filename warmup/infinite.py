#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    in_as = s.count('a')
    remain_as = 0

    remainer = n % len(s)

    if remainer != 0:
        remain_as = s[0:remainer].count('a')

    return int(in_as * (abs(n/len(s))) + remain_as)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'aba'

    n = int(10)

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()