class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        dp_cache = [[None] * n for _ in range(m)]
        curr_max = 0
        def dp(i, j):
            nonlocal curr_max
            if i == 0 or j == 0:
                dp_cache[i][j] = 0
            else:
                if dp_cache[i][j] is None:
                    if matrix[i - 1][j - 1] == '1':
                        dp_cache[i][j] = min(dp(i - 1, j - 1), dp(i, j - 1), dp(i - 1, j)) + 1
                        curr_max = max(dp_cache[i][j], curr_max)
                    else:
                        dp_cache[i][j] = 0
            return dp_cache[i][j]
        for i in range(m):
            for j in range(n):
                dp(i, j)
        return curr_max ** 2
