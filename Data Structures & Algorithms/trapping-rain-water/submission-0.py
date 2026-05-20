class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        lm = 0 
        rm = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                lm = max(lm, height[l])
                water += lm - height[l]
                l += 1
            else: 
                rm = max(rm, height[r])
                water += rm - height[r]
                r -= 1
        return water

        