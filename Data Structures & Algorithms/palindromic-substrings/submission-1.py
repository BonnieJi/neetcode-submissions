class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        seen = set()
        for i in range(n):
            l, r = i, i
            while l>= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            l, r = i, i+1
            while l>= 0 and r < n and  s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res
            





        # n, res = len(s), 0
        # dp = [[False]* n for _ in range(n)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i,n):
        #         if s[i] == s[j] and (j-i <=2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             res += 1
        # return res
        