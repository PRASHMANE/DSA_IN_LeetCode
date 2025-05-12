class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        val=0
        lst=set(nums)
        for i in lst:
            if nums.count(i) > count:
                count = nums.count(i)
                val = i
        return val