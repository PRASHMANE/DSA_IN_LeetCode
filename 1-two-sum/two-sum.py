class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}
        n = len(nums)
        for i in range(n):
            val = target-nums[i]
            if val in hash:
                return [i,hash[val]]
            hash[nums[i]]=i
        return [-1.-1]
        

        


        