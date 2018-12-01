#!/bin/python

import math
import os
import random
import re
import sys


def median(expenditure):



# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    median = 'even' if d % 2 == 0 else 'odd'
    notif = 0
    n = len(expenditure)

    for day in xrange(n-d):
        exp_4_med = expenditure[day:day+d]
        exp_4_med.sort()
        if median == 'even':
            exp_med = float(exp_4_med[day+d/2-1] + exp_4_med[day+d/2]) / 2
        elif median == 'odd':
            exp_med = float(exp_4_med[day+d/2-1])
        if expenditure[day+d] >= exp_med*2:
            notif += 1
        # print 'exp', expenditure[day+d], exp_4_med, 'notif=', notif

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
