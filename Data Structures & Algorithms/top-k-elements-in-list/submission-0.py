class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d: d[n] = d[n] + 1
            else: d[n] = 1
        sorted_items = sorted(d.items(), key=lambda x: x[1])
        return [num for num, freq in sorted_items[-k:]]

