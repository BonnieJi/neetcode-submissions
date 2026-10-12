class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if profit[i] != -1:
                return profit[i]
            profit[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return profit[i]
        return max(dfs(0),dfs(1))