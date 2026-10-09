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
            j = i
            while j < len(nums)-1 and nums[i] == nums[j+1]:
                j += 1
            dfs(j+1, curr, total)
        dfs(0, [], 0)
        return res
        