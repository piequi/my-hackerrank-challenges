#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    # index s1
    s1_idx = {}
    for c in s1:
        if c in s1_idx:
            s1_idx[c] += 1
        else:
            s1_idx[c] = 1

    # index s2
    s2_idx = {}
    for c in s2:
        if c in s2_idx:
            s2_idx[c] += 1
        else:
            s2_idx[c] = 1

    # compare 2 index (using s2)
    for c in s2_idx.keys():
        if c in s1_idx.keys():
            print 'YES'
            return 'YES'
    print 'NO'
    return 'NO'



if __name__ == '__main__':
    fptr = open('out', 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
