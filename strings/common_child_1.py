#!/bin/python

import math
import os
import random
import re
import sys
import time

# Complete the commonChild function below.


def commonChild(s1, s2):
    size = len(s1)
    if s1 == s2:
        return size
    elif size == 0:
        return 0
    else:
        max_child = 0
        for i in range(size):
            new_s1 = s1[0:i] + s1[i+1:size]
            for j in range(size):
                new_s2 = s2[0:j] + s2[j+1:size]

                child_size = commonChild(new_s1, new_s2)
                if child_size > max_child:
                    max_child = child_size
        return max_child



if __name__ == '__main__':
    fptr = open('out', 'w')

    s1 = raw_input()

    s2 = raw_input()


    result = commonChild(s1, s2)
    print 'result=', result
    fptr.write(str(result) + '\n')

    fptr.close()
