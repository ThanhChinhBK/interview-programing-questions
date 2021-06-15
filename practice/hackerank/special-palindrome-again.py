#!/bin/python3

import math
import os
import random
import re
import sys

def substrCount(n, s):
    c = n
    valided_str = set()
    for i in range(n):
        j = i
        while j < n-1:
            j += 1
            if s[j] == s[i]:
                c += 1
            else:
                if s[i:j] == s[j+1:j+1+j-i]:
                    c  += 1
                break
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

