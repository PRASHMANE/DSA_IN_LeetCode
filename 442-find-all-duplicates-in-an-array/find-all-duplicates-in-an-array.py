class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        count=Counter(nums)
        for i , j in count.items():
            if j > 1:
                ans.append(i)
        return ans