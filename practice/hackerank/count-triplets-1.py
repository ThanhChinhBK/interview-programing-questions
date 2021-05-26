
import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

def countTriplets(arr, r):
    bf = Counter()
    af = Counter(arr)
    c = 0
    for i in arr:
        af[i] -=1
        if i % r== 0 and bf[i//r] > 0 and af[i*r] > 0:
            c += bf[i//r] * af[i*r]
        bf[i]+=1
    return c
        
               
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
