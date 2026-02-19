class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def count_sum(arr,mid):
            split=1
            total=0

            for i in range(len(arr)):
                if total + arr[i] <= mid:
                    total+=arr[i]
                else:
                    split+=1
                    total=arr[i]
            
            return split

        if len(nums) < k:
            return -1 
        
        low = max(nums)
        high=sum(nums)
        ans = -1

        while low <= high:
            mid=(low+high)//2
            if count_sum(nums,mid) > k:
                low=mid+1
            else:
                ans = mid
                high=mid-1
        
        return ans

        