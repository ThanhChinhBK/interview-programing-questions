#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    print("    ")
    dp = [0] * (len(arr))
    dp[0] = arr[0]
    max_seq_sum = arr[0]
    cur_seq_sum = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(dp[i - 1] + arr[i], dp[i - 1], arr[i])
        cur_seq_sum = cur_seq_sum + arr[i]
        max_seq_sum = max(max_seq_sum, cur_seq_sum, arr[i])
        if cur_seq_sum < 0:
            cur_seq_sum = 0
        

    return max_seq_sum, dp[-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

