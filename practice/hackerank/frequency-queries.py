#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    res = []
    a = defaultdict(int)
    b = defaultdict(int)
    for query in queries:
        if query[0] == 1:
            b[a[query[1]]] -= 1
            a[query[1]] += 1
            b[a[query[1]]] += 1
        elif query[0] == 2:
            if a[query[1]] > 0:
                b[a[query[1]]] -= 1
                a[query[1]] -= 1
                b[a[query[1]]] += 1 
        elif query[0] == 3:
            if b[query[1]] > 0:
                res.append(1)
            else:
                res.append(0)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
