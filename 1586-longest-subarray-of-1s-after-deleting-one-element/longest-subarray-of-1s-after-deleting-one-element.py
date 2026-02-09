class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left=0
        maxlen=0
        n=len(nums)
        zero=0

        for right in range(n):

            if nums[right]==0:
                zero+=1

            while zero > 1 :
                if nums[left] == 0:
                    zero-=1
                left+=1
            
            if zero <= 1 :
                maxlen=max(maxlen,right-left+1)
            
        return maxlen-1
            
