class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = 1
        count = 1
        nums.sort()

        n = len(nums)
        if n == 0:
            return 0

        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                count+=1
            elif nums[i] != nums[i-1]:
                count=1
            length = max(length,count)
        return length

