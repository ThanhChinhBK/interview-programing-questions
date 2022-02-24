from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(len(s) + 1)
        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 0 if s[0] == '0' else 1
            res = 0
            if 9 < int(s[i - 2: i]) <= 26:
                res += dp(i - 2)
            if 0 < int(s[i-1: i]):
                res += dp(i - 1)
            return res
        return dp(len(s))
