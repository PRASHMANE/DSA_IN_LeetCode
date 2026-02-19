class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # Try x from 1 to n
        for x in range(1, n + 1):
            # Binary search to find first index >= x
            idx = bisect_left(nums, x)
            count = n - idx
            if count == x:
                return x
        return -1