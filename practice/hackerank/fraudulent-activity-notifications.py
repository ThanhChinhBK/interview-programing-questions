#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    notify_count = 0
    arr_dict = {}
    def medium(idx):
        freqs = 0
        for i in range(201):
            if i in arr_dict:
                freqs += arr_dict[i]
                
                if freqs >= idx:
                    return i
            
    for i in range(len(expenditure)):
        if i >= d:
            if d%2 == 0:
                med = medium(d//2)  + medium(d//2 + 1)
            else:
                med =  2 * medium(d//2 + 1)
            if expenditure[i] >= med:
                notify_count += 1
            arr_dict[expenditure[i-d]] -= 1
        if expenditure[i] not in arr_dict:
            arr_dict[expenditure[i]] = 1
        else:
            arr_dict[expenditure[i]] += 1
        
    return notify_count
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

