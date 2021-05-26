#!/bin/python3
# https://www.hackerrank.com/challenges/crush/problem
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    curr_arr = [0] * n
    for query in queries:
        for i in range(query[0]-1, query[1] ):
            curr_arr[i] += query[2]
    return max(curr_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

