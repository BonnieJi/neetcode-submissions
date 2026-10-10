class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def dfs(perm, picked):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            for i in range(len(nums)):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True
                    dfs(perm,picked)
                    picked[i] = False
                    perm.pop()
        dfs([], [False]*len(nums))
        return res




        # res = []
        # def dfs(perm, pick):
        #     if len(perm) == len(nums):
        #         res.append(perm[:])
        #         return 
        #     for i in range(len(nums)):
        #         if not pick[i]:
        #             perm.append(nums[i])
        #             pick[i] = True
        #             dfs(perm,pick)
        #             perm.pop()
        #             pick[i] = False
        # dfs([], [False]*len(nums))
        # return res