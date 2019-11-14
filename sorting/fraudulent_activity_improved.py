#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    def getMedian(e, a, b):
        trail = e[a:b]
        trail.sort()
        nbtrail = int(b-a)
        if nbtrail % 2 != 0:
            m = trail[int(nbtrail/2) + 1]
        elif nbtrail % 2 == 0:
            m = (trail[int(nbtrail/2 - 1)] + trail[int(nbtrail/2)]) / 2
        return m

    notifications = 0
    nbexpenditure = len(expenditure)

    for exp in range(d, nbexpenditure):
        median = getMedian(expenditure, exp-d, exp-1)
        if expenditure[exp] > median * 2:
            notifications += 1

    return notifications


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)
