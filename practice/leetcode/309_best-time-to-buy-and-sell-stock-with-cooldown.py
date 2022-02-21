from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache((n + 1) * 4)
        def dp(i, is_holding, is_cooldown):
            if i == n:
                return 0
            if is_cooldown:
                return dp(i + 1, False, False)
            if is_holding:
                return max(dp(i + 1, is_holding, is_cooldown),
                           prices[i] + dp(i + 1, False, True))
            else:
                return max(dp(i + 1, is_holding, is_cooldown),
                           -prices[i] + dp(i + 1, True, False))
        return dp(0, False, False)
            
