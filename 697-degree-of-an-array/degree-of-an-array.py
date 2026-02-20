class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}

        # First pass: record first/last positions, and frequencies
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())   # overall degree
        res = len(nums)

        # Find shortest interval among elements with degree
        for x in count:
            if count[x] == degree:
                res = min(res, right[x] - left[x] + 1)

        return res