class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def sumlessk(arr,k):

            if k < 0:
                return 0

            left=0
            n=len(arr)
            count=0

            sum1=0
            for right in range(n):
                sum1+=arr[right]

                while sum1 > k:
                    sum1-=arr[left]
                    left+=1
                
                if sum1 <= k:
                    count += right-left+1
            
            return count
        
        return sumlessk(nums,goal)-sumlessk(nums,goal-1)
        