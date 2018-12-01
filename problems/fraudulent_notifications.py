#!/bin/python

import math
import os
import random
import re
import sys


def computeMedian(sorted_exp, d, median):

    if median == 'even':
        return float(sorted_exp[d/2-1] + sorted_exp[d/2]) / 2
    elif median == 'odd':
        return float(sorted_exp[d/2])


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    median = 'even' if d % 2 == 0 else 'odd'
    notif = 0
    n = len(expenditure)
    trailing = expenditure[:d]
    sorted_trailing = trailing[:]
    sorted_trailing.sort()

    for expense in expenditure[d:n+1]:
        # print 'trailing=', trailing
        # print 'sorted_trailing=', sorted_trailing
        # print 'expense=', expense
        # print 'med=', median, computeMedian(sorted_trailing, d, median)
        if expense >= computeMedian(sorted_trailing, d, median)*2:
            notif += 1
        # insert expense at the right place in sorted trailing
        t = 0
        inserted = 0
        while t < d and inserted == 0:
            if expense <= sorted_trailing[t]:
                sorted_trailing.insert(t, expense)
                inserted = 1
            t += 1
        if inserted == 0:
            sorted_trailing.append(expense)
        # update trailing lists expense
        sorted_trailing.remove(trailing[0])
        trailing.append(expense)
        trailing = trailing[1:]

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
