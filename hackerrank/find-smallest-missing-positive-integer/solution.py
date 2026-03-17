#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#


def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    if n == 0:
        return 1

    i = 0
    while i < n:
        elem = orderNumbers[i]

        if elem <= 0 or elem > n or elem == orderNumbers[elem - 1] or elem == i + 1:
            i += 1
            continue

        orderNumbers[elem - 1], orderNumbers[i] = elem, orderNumbers[elem - 1]

    for i, elem in enumerate(orderNumbers):
        if elem - 1 != i:
            return i + 1

    return n + 1


if __name__ == "__main__":
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
