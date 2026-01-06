class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=sum(nums)
        n=len(nums)
        total=n*(n+1)//2
        return total-sum1
        