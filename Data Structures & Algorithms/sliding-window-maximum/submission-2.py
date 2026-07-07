class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        
        # Left max
        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
        
        # Right max
        for i in range(n-1, -1, -1):
            if i == n-1 or (i+1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i+1], nums[i])
        
        # Sliding window max
        output = []
        for i in range(n - k + 1):
            output.append(max(right[i], left[i + k - 1]))
        
        return output