class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        ans=[]
        for i in digits:
            s+=str(i)
        s=str(int(s)+1)
        for i in s:
            ans.append(int(i))
        return ans

        