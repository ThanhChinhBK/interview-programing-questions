#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_at_i = [None] * len(arr)
    max_at_i[0], max_at_i[1] = arr[0], max(arr[0], arr[1])
    for i in range(2, len(arr)):
        max_at_i[i] =  max(max_at_i[i-1], max_at_i[i-2]+arr[i], arr[i])
    return max_at_i[len(arr)-1]
        
    return max_
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

