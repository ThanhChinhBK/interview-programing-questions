from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(len(s))
        def dp(i):
            if i == 0:
                return True
            trials = []
            for word in wordDict:
                if s[:i].endswith(word):
                    trials.append(dp(i - len(word)))
            if not trials:
                return False
            return sum(trials)
        return dp(len(s))
