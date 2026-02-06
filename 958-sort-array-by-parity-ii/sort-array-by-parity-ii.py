class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        ans=[]
        for i,j in zip(even,odd):
            ans.append(i)
            ans.append(j)
        return ans