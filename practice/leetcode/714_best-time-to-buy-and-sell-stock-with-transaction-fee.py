from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(len(prices) * 2)
        def dp(i, is_holding):
            if i == len(prices):
                return 0
            if is_holding:
                return max(dp(i + 1, True), prices[i] - fee + dp(i + 1, False))
            else:
                return max(dp(i + 1, False), -prices[i] + dp(i + 1, True))
        return dp(0, False)
