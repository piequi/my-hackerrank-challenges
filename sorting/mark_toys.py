#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):

    prices.sort()

    nPrices = len(prices)
    maxToys = 0
    idx1 = idx2 = 0
    sumPrices = prices[idx1]
    while idx1 < nPrices and prices[idx1] <= int(k):
        sumPrices = prices[idx1]
        toys = 1
        idx2 = idx1 + 1
        while idx2 < nPrices and (sumPrices + prices[idx2]) <= int(k):
            sumPrices += prices[idx2]
            toys += 1
            idx2 += 1
        if toys > maxToys:
            maxToys = toys
        idx1 += 1

    return maxToys


if __name__ == '__main__':
    fptr = open('out_mark_toys', 'w')

    n, k = input().split()

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()