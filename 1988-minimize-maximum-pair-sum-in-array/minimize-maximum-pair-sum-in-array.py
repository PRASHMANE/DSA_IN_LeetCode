class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums)-1
        ans=0
        for i in range(len(nums)//2):
            ans=max(ans,nums[i]+nums[right-i])
        return ans


        