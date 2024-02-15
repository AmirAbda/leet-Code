class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def lcs(i, j):
            if i == 0 or j == 0:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if text1[i - 1] == text2[j - 1]:
                memo[i][j] = 1 + lcs(i - 1, j - 1)
            else:
                memo[i][j] = max(lcs(i - 1, j), lcs(i, j - 1))
            return memo[i][j]

        return lcs(m, n)