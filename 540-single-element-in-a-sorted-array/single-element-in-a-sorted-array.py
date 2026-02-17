class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n=len(nums)

        if n == 1:
            return nums[0]

        low = 1
        high = n-2

        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        while low <= high:
            mid = (low+high)//2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid] 

            if mid % 2 == 0: # even
                if nums[mid] == nums[mid+1]: # even odd
                    low = mid+1
                elif nums[mid] == nums[mid-1]: # odd even
                    high = mid-1
                
            else: # odd

                if nums[mid] == nums[mid+1]: #  odd even
                    high = mid-1
                elif nums[mid] == nums[mid-1]: # even odd
                    low = mid+1
                

