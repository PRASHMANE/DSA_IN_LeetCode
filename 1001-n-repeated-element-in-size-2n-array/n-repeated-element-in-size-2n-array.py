class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i in ans:
                return i
            ans.append(i)