class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n - 1):
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_left(nums, upper - nums[i] + 1, i + 1, n)
            ans += (right - left)

        return ans