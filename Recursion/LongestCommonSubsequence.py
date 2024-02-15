class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        def lcs(i, j):
            if i == 0 or j == 0:
                return 0
            if text1[i - 1] == text2[j - 1]:
                 return 1 + lcs(i - 1, j - 1)
            else:
                return max(lcs(i - 1, j), lcs(i, j - 1))
        return lcs(m,n)
        
        