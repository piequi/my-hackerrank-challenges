#!/bin/python

# from __future__ import print_function

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hr = int(s[:2])
    am_pm = s[-2:]

    if am_pm == 'PM':
        hr += 12

    return str(hr) + s[2:8]



if __name__ == '__main__':
    f = open('out', 'w')

    s = raw_input()

    result = timeConversion(s)
    print result
    f.write(result + '\n')

    f.close()
