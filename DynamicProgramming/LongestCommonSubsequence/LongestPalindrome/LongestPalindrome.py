class Solution:
    def longestPalindrome(s):
        n=len(s)
        dp=[[[0]*(n+1)] for _ in range(n+1) ]
        for i in range(n+1):
            for j in range(n+1):
                # diagrongal 
                if s[i]==s[j]:
                    dp[i][j]=1
                