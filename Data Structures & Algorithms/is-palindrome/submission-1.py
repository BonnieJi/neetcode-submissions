class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for _ in s: 
            if _.isalnum():
                s1 += _.lower()
        return s1[::-1] == s1
