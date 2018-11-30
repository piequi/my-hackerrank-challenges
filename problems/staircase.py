#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    steps = [" " for _ in range(n)]
    for l in range(n, 0, -1):
        steps[l-1] = "#"
        print ''.join(steps)

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
