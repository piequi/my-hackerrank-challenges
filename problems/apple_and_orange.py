#!/bin/python3

import math
import os
import random
import re
import sys
import typing

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges) -> None:
    count_fruits_in_house(s, t, a, apples)
    count_fruits_in_house(s, t, b, oranges)

def count_fruits_in_house(house_start:int, house_end:int, tree_location:int, fruits_distances: list[int]) -> None:
    print_fruits_count_in_house(house_start, house_end, compute_fruits_locations(tree_location, fruits_distances))

def compute_fruits_locations(tree_location: int, fruits_distances: list[int]) -> list[int]:
    locations: list[int] = []
    for distance in fruits_distances:
        locations.append(tree_location + distance)
    return locations

def print_fruits_count_in_house(house_start: int, house_end: int, fruits_locations: list[int]) -> None:
    counter: int = 0
    for location in fruits_locations:
        if house_start <= location <= house_end:
            counter += 1
    print(counter)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
