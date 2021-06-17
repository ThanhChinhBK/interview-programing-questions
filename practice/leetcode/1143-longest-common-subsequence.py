class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # Write your code here
        n1 = len(s1)
        n2 = len(s2)
        L = [[None] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    L[i][j] = 1 + L[i-1][j-1]
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[n1][n2]
        
