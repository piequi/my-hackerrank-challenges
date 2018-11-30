#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    # index magazine words
    magazine_idx = {}
    for word in magazine:
        if word in magazine_idx:
            magazine_idx[word] += 1
        else:
            magazine_idx[word] = 1

    # index note words
    note_idx = {}
    for word in note:
        if word in note_idx:
            note_idx[word] += 1
        else:
            note_idx[word] = 1

    # compare 2 index (using note)
    for word, count in note_idx.items():
        if word in magazine_idx.keys():
            if magazine_idx[word] < count:
                print 'No'
                return
        else:
            print 'No'
            return

    # print yes if end of note index is reached
    print 'Yes'
    return

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().split()

    note = raw_input().split()

    checkMagazine(magazine, note)
