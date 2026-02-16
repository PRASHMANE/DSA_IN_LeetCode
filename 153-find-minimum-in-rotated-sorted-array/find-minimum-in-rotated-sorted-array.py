class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n=len(nums)
        low=0
        high=n-1

        minans=float('inf')

        while low <= high:
            mid=(low+high)//2

            if nums[low] <= nums[mid]:
                minans=min(minans,nums[low])
                low=mid+1
            else:
                minans=min(minans,nums[mid])
                high=mid-1
        return minans
        