#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    dp = [[False for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    
    dp[0][0] = True
    i = 1
    while i <= len(a) and a[i - 1].islower():
        dp[i][0] = True
        i += 1
        
    for i in range(1, len(a) + 1):
        for j in range(1, min(i, len(b)) + 1):
            if a[i - 1].islower():
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if a[i - 1].upper() == b[j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
    
    if dp[len(a)][len(b)]:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
