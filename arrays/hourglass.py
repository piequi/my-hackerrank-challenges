#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_i = len(arr)
    max_j = len(arr[0])
    max_sum = -54
    print (arr)

    if max_i >= 3 and max_j >= 3:
        for i in range(max_i -2):
            for j in range(max_j - 2):
                hg_sum = int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2]) \
                         + int(arr[i+1][j+1]) \
                         + int(arr[i+2][j]) + int(arr[i+2][j+1]) + int(arr[i+2][j+2])
                if hg_sum > max_sum:
                    max_sum = hg_sum
    # print max_sum
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[-1, -1, 0, -9, -2, -2],[-2, -1, -6, -8, -2, -5],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
    # arr = [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0], [0,0,2,4,4,0], [0,0,0,2,0,0], [0,0,1,2,4,0]]
    # arr = []
    #
    # for _ in xrange(6):
    #     arr.append(map(int, "['1 1 1 0 0 0', '0 1 0 0 0 0', '1 1 1 0 0 0', '0 0 2 4 4 0', '0 0 0 2 0 0', '0 0 1 2 4 0']".rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()