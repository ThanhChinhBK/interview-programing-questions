import functools

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        hardest_at_i = []
        for i in range(n):
            hardest_at_i.append(max(jobDifficulty[i:]))
        
        @functools.lru_cache(d * i)
        def dp(day, i):
            if day == d - 1:
                return hardest_at_i[i]
            else:
                hardest = 0
                res = float("inf")
                for j in range(i, n - (d - day) + 1):
                    hardest = max(hardest, jobDifficulty[j])
                    res = min(res, hardest + dp(day + 1, j + 1))
                return res
        return dp(0, 0)
