#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here

    seqList = []
    for idx in range(n):
        seqList.append([])
    lastAnswer = 0
    result = []

    for query in queries:
        x = query[1]
        y = query[2]
        seqIndex = (x ^ lastAnswer) % n

        if query[0] == 1:
            seqList[seqIndex].append(y)

        elif query[0] == 2:
            elementIndex = y % len(seqList[seqIndex])
            lastAnswer = seqList[seqIndex][elementIndex]
            #print(lastAnswer)
            result.append(lastAnswer)

    return result


if __name__ == '__main__':
    fptr = open('out_dynamic_array', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
