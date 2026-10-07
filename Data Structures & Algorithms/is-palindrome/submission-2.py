class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # skip non-alphanumeric from the left
            while l < r and not s[l].isalnum():
                l += 1
            # skip non-alphanumeric from the right
            while l < r and not s[r].isalnum():
                r -= 1

            # compare case-insensitively
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
