class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lowerbound(arr,n,k):
            ans=n
            low=0
            high=n-1

            while low <= high:
                mid = (low+high)//2

                if arr[mid] >= k:
                    ans=mid
                    high=mid-1
                else:
                    low = mid+1
            return ans

        def upperbound(arr,n,k):
            ans=n
            low=0
            high=n-1

            while low <= high:
                mid = (low+high)//2

                if arr[mid] > k:
                    ans=mid
                    high=mid-1
                else:
                    low = mid+1
            return ans
        

        n = len(nums)
        lb = lowerbound(nums,n,target) 

        if lb == n or nums[lb] != target:
            return [-1,-1]
        
        ub = upperbound(nums,n,target)

        return [lb,ub-1]