#!/bin/python

import math
import os
import random
import re
import sys



# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    colors = {}
    socks = list(ar)
    print('socks = ', socks)

    for s in socks:
        colors[s] = 0

    for color in socks:
        colors[color] += 1
        if (colors[color] % 2) == 0:
            pairs += 1
            colors[color] = 0
    print('after: ', colors)

    print('pairs', pairs)

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(9)

    ar = map(int, "10 20 20 10 10 30 50 10 20".rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
