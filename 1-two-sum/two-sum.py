class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh={}
        for i,num in enumerate(nums):
            com = target - num
            if com in hsh:
                return [hsh[com],i]
            hsh[num] = i



        