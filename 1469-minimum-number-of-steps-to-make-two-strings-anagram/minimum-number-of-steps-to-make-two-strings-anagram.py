class Solution:
    def minSteps(self, s: str, t: str) -> int:

        count = Counter(t)
        ans=0

        for i in s:
            if count.get(i,0) == 0:
                ans+=1
            else:
                count[i]-=1
        
        return ans
        