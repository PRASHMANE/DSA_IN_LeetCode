class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        pos=[]
        neg = []

        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        for i,j in zip(pos,neg):
            ans.append(i)
            ans.append(j)
        
        return ans
        