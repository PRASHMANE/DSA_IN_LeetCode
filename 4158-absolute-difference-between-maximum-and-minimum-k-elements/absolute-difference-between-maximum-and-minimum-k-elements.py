class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        if k == 1 and len(nums) == 1:
            return 0
        if len(nums) < k:
            return 0
        
        return abs(sum(nums[:k])-sum(nums[::-1][:k]))