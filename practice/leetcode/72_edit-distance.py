class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L = [[None for _ in range(len(word2) +1)] for _ in range(len(word1)+1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    L[i][j] = j
                elif j == 0:
                    L[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    L[i][j] = L[i-1][j-1]
                else:
                    L[i][j] = min(L[i-1][j-1], L[i][j-1], L[i-1][j]) + 1
        return L[len(word1)][len(word2)]
