#!/bin/python

# from __future__ import print_function

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(':')
    hr = time[0]

    if time[2][-2:] == 'PM' and hr != '12':
        hr = int(hr) + 12
    elif time[2][-2:] == 'AM' and hr == '12':
        hr = '00'

    return str(hr) + ':' + time[1] + ':' + time[2][:2]



if __name__ == '__main__':
    f = open('out', 'w')

    s = raw_input()

    result = timeConversion(s)
    print result
    f.write(result + '\n')

    f.close()
