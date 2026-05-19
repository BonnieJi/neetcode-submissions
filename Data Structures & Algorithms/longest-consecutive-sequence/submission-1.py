class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for num in nset: 
            if num - 1 not in nset: 
                length = 1
                while num + length in nset: 
                    length += 1
                longest = max(longest, length)
        return longest 
        



        