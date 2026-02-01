class Solution:
    def findLHS(self, nums):
        fre=Counter(nums)
        ans=0

        for num in fre:
            if num+1 in fre:
                ans=max(ans,fre[num]+fre[num+1])
        return ans