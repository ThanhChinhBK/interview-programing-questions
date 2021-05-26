#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isAnagram(s1, s2):
    return tuple(sorted(s1)) == tuple(sorted(s2))
def sherlockAndAnagrams(s):
    # Write your code here
    anagrams_dict = Counter()
    for i in range(len(s)-1):
        for j in range(i+1, len(s)+2):
            curr_s = s[i:j]
            for x in range(i+1, len(s) - len(curr_s)+1):
                if isAnagram(curr_s, s[x: x+ len(curr_s)]):
                    anagrams_dict[tuple(sorted(curr_s))] += 1
    return sum(anagrams_dict.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

