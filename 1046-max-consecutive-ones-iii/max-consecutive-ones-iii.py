class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zero=0
        left=0
        right=0
        maxlen=0
        n= len(nums)

        while right < n:
            if nums[right] == 0:
                zero+=1
            
            if zero > k:
                if nums[left] == 0:
                    zero-=1
                left+=1
            
            if zero <= k:
                maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen