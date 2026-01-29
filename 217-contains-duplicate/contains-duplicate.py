class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hst={}
        for i in nums:
            if i in hst:
                return True
            else:
                hst[i] = 1
        return False
        