# Given an array, find the length of the longest switching slice.

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if n <= 2:
        return n
    longest = 2
    tmp_longest = 2
    for ind in range(2, n):
        if A[ind-2] == A[ind]:
            tmp_longest += 1
        else:
            tmp_longest = 2
        longest = max(tmp_longest, longest)
    return longest
