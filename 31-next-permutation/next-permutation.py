class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1

        n=len(nums)

        for i in range(n-1):
            if nums[i] < nums[i+1]:
                ind=i
            
        
        if ind != -1:
            for i in range(n-1,ind,-1):
                if nums[ind] < nums[i]:
                    nums[ind],nums[i]=nums[i],nums[ind]
                    break
            nums[ind+1:]=nums[ind+1:][::-1]
        else:
            nums[:] = nums[::-1]