class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zero_count=0
        maxlen=0
        left=0

        n=len(nums)

        for right in range(n):

            if nums[right] == 0:
                zero_count+=1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        
        return maxlen
        