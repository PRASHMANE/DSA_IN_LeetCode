class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        n=len(nums)
        for i in count:
            if count[i] > n//2:
                return i
                