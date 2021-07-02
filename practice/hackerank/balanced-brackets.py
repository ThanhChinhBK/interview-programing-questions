#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    brackets = []
    reverse_symbols = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    for c in s:
        if c in "{([":
            brackets.append(c)
        elif c in "]})":
            if not len(brackets):
                return "NO"
            if brackets[-1] != reverse_symbols[c]:
                return "NO"
            else:
                brackets.pop()
    if len(brackets):
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

