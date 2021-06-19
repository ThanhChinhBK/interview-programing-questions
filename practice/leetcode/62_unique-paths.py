from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n ==1 or m == 1:
            return 1
        return comb(m + n - 2, m - 1)
