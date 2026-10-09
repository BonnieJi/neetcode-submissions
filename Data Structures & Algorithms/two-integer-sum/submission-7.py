class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, n in enumerate(nums):
            index[n] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index and index[diff] != i:
                return [i, index[diff]]




        