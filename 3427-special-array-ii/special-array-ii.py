class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        prefix=[0]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]+(nums[i]%2 == nums[i-1]%2)

        ans=[]
        for i, j in queries:
            ans.append(prefix[j]-prefix[i]==0)
        return ans        