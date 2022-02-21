from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(k * (n + 1) * 2)
        def dp(transaction_remain, i, is_holding):
            if transaction_remain == 0:
                return 0
            if i == n:
                return 0
            if is_holding:
                return max(dp(transaction_remain, i + 1, True),
                           prices[i] + dp(transaction_remain - 1, i + 1, False))
            else:
                return max(dp(transaction_remain, i+1, False),
                           - prices[i] + dp(transaction_remain, i + 1, True))
        return dp(k, 0, False)
