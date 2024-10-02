#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note) -> None:
    # count magazine words
    magazine_words: dict[str: int] = {}
    for word in magazine:
        if word in magazine_words.keys():
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    # find note words in magazine words
    all_words_found: str = "Yes"
    for word in note:
        if word not in magazine_words.keys():
            all_words_found = "No"
        else:
            # remove word instance when found
            magazine_words[word] -= 1
            if magazine_words[word] == 0:
                del magazine_words[word]

    # print result
    print(all_words_found)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
