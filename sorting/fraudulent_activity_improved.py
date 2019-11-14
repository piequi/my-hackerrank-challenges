#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    def getMedian(v, d):
        median = 0
        if d % 2 != 0:
            median_pos = int(d/2) + 1
            for value, count in v.items():
                if median_pos > 0:
                    median_pos -= count
                    median = value
                else:
                    break
        elif d % 2 == 0:
            median1 = median2 = 0
            median_pos1 = int(d/2)
            median_pos2 = int(d/2) + 1
            for value, count in v.items():
                if median_pos1 > 0:
                    median_pos1 -= count
                    median1 = value

                if median_pos2 > 0:
                    median_pos2 -= count
                    median2 = value
                else:
                    break
            median = (median1 + median2) / 2

        return median

    notifications = 0
    nbexpenditure = len(expenditure)
    valueshash = {}

    for exp in range(nbexpenditure):
        if expenditure[exp] in valueshash:
            valueshash[expenditure[exp]] += 1
        else:
            valueshash[expenditure[exp]] = 1
        if exp >= d:
            median = getMedian(valueshash, d)
            if expenditure[exp] >= median * 2:
                notifications += 1
            valueshash[expenditure[exp-d]] -= 1


    return notifications


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)
