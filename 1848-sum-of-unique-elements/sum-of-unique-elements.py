class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        count=Counter(nums)
        sum=0

        for key,value in count.items():
            if value == 1:
                sum+=key
        return sum