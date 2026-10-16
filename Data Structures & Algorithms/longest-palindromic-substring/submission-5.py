class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        for i in range(len(s)):
            r, l = i,i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resIdx = l
                    resLen = r-l+1
                l-= 1
                r += 1
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resIdx = l
                    resLen = r-l+1
                l-= 1
                r+= 1
        return s[resIdx:resIdx+resLen]

        # n = len(s)
        # resIdx, resLen = 0,0
        # dp = [[False]*n for _ in range(n)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i,n):
        #         if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             if resLen < (j-i+1):
        #                 resIdx = i
        #                 resLen = j-i + 1
        # return s[resIdx: resIdx+resLen]