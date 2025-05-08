class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2 != 0:
            return False
        for i in nums:
            count=nums.count(i)
            if count%2 != 0:
                return False
        return True
        