class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = set()
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights):
                area.add((i-j)* min(h1, h2))
        return max(area)
        