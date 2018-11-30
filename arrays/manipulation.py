#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    elements = [0 for _ in range(n)]
    max_result = 0
    for query in queries:
        for i in xrange(query[0], query[1]+1):
            elements[i-1] += query[2]
            if elements[i-1] > max_result:
                max_result = elements[i-1]

    return max_result

if __name__ == '__main__':
    fptr = open('manipulation.out', 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
