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
    else:
        max_child = 0
        c = 1
        while c < (size - max_child):
            print "remove", c
            for i in range(size-c+1):

                new_s1 = s1[0:i] + s1[i+c:size]

                for j in range(size-c+1):
                    new_s2 = s2[0:j] + s2[j+c:size]

                    print 'i=',i,'new_s1=',new_s1
                    print 'j=',j,'new_s2=',new_s2

                    if new_s1 == new_s2 and len(new_s1) > max_child:
                        max_child = len(new_s1)
                        print 'max_child=', max_child
            # try removing more characters
            c += 1

        return max_child



if __name__ == '__main__':
    fptr = open('out', 'w')

    s1 = raw_input()

    s2 = raw_input()


    result = commonChild(s1, s2)
    print 'result=', result
    fptr.write(str(result) + '\n')

    fptr.close()
