import functools

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(S):
            if S == 0: return 0
            if S < 0 : return -1
            trials = []
            for coin in coins:
                trial_res = dp(S - coin)
                if trial_res >= 0:
                    trials.append(trial_res)
            if trials:
                return min(trials) + 1
            return -1
        return dp(amount)
