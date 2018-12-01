#!/bin/python

import math
import os
import random
import re
import sys


def computeMedian(expenditure, d, median):

    expenditure.sort()
    if median == 'even':
        return float(expenditure[d/2-1] + expenditure[d/2]) / 2
    elif median == 'odd':
        return float(expenditure[d/2])


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    median = 'even' if d % 2 == 0 else 'odd'
    notif = 0
    n = len(expenditure)
    trailing = expenditure[:d]

    for expense in expenditure[d:n+1]:
        # print 'trailing=', trailing
        # print 'expense=', expense
        if expense >= computeMedian(trailing[:], d, median)*2:
            notif += 1
        trailing = trailing[1:]
        trailing.append(expense)

    return notif


if __name__ == '__main__':
    fptr = open('out', 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = map(int, raw_input().rstrip().split())

    result = activityNotifications(expenditure, d)
    print result
    fptr.write(str(result) + '\n')

    fptr.close()
