#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    value_dict = {}
    for i, cost_1 in enumerate(cost):
        cost_2 = money - cost_1
        if cost_2 in value_dict:
            print(value_dict[cost_2] + 1, i + 1)
        value_dict[cost_1] = i


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
