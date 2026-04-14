class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = n-2

        while (ind >= 0 and nums[ind]>=nums[ind+1]):
            ind-=1
        
        if ind >= 0:
            j = n-1
            for i in range(j,-1,-1):
                if nums[i] > nums[ind]:
                    break
            
            nums[ind],nums[i] = nums[i],nums[ind]
        
        nums[ind+1:] = nums[ind+1:][::-1]
        return nums
