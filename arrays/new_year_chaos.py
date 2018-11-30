#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    last_index = len(q) - 1
    queue = q
    swaps_count = 0
    start_queue = list(range(1, len(q)+1))

    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            print "Too chaotic"
            return

    while queue != start_queue:
        for i in range(last_index):
            if queue[i] > queue[i+1]:
                # do swap
                tmp = queue[i+1]
                queue[i+1] = queue[i]
                queue[i] = tmp
                # count swap
                swaps_count += 1

    print swaps_count
    return


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
