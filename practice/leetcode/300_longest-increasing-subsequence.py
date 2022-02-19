from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(n)
        def dp(i):
            trials = [1]
            for j in range(i):
                if nums[i] > nums[j]:
                    trials.append(dp(j) + 1)
            return max(trials)
        return max(dp(i) for i in range(n))
