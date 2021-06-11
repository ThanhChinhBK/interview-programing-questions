#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(array_):
    count = 0
    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        n = len(arr)
        sorted1 = mergeSort(arr[:n//2])
        sorted2 = mergeSort(arr[n//2:])
        final = merge(sorted1, sorted2)
        return final
        
    def merge(arr1, arr2):
        nonlocal count
        curr2 = 0
        final = []
        for curr1 in range(len(arr1)):
            while curr2 < len(arr2) and arr1[curr1] > arr2[curr2]:
                final.append(arr2[curr2])
                curr2 += 1
                count += len(arr1) - curr1
            final.append(arr1[curr1])
        final += arr2[curr2:]
        return final
    mergeSort(array_)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

