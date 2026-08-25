class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0
        maxi = 0

        n = len(nums)

        for right in range(n):
            sum+=nums[right]
            if sum < 0:
                sum = 0
            maxi = max(maxi,sum)
        return maxi if maxi != 0 else max(nums)