class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target or i >= len(nums):
                return 
            curr.append(nums[i])
            dfs(i+1, curr, total + nums[i])
            curr.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, curr, total)
        dfs(0, [], 0)
        return res
        