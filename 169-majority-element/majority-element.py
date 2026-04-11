class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        can = 0
        for num in nums:
            if count == 0:
                can = num
            if num == can:
                count+=1
            else:
                count-=1
        return can