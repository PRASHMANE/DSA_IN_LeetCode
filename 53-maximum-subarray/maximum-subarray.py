class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum=0
        maxsum=0
        n=len(nums)

        for i in range(n):

            sum+=nums[i]

            if sum < 0:
                sum = 0
            
            maxsum=max(sum,maxsum)
        
        return maxsum if maxsum != 0 else max(nums)
            



        