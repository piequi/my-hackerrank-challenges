#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    string_size = len(s)
    anagrams = 0

    if string_size > 1:

        for substring_size in xrange(1, string_size):
            # on compare les substrings 1 a 1 en partant de la 1ere
            for substring1_start_index in xrange(0, string_size-substring_size):
                substring1 = s[substring1_start_index:substring1_start_index+substring_size]
                for substring2_start_index in xrange(substring1_start_index+1, string_size-substring_size+1):
                    substring2 = s[substring2_start_index:substring2_start_index+substring_size]
                    anagrams += areAnagrams(substring1, substring2)

    return anagrams

def areAnagrams(s1,s2):
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

    # compare index
    if s2_idx == s1_idx:
            return 1
    else:
        return 0


if __name__ == '__main__':
    fptr = open('out', 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)
        print result
        fptr.write(str(result) + '\n')

    fptr.close()
