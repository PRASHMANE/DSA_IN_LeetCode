from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        digt=defaultdict(list)
        n=len(nums)
        m=len(nums[0])


        for i in range(len(nums)):
            for j in range(len(nums[i])):
                val=nums[i][j]
                digt[i+j].append(val)
        
        for i in range(max(digt.keys())+1):
            ans.extend(digt[i][::-1])
        return ans
        