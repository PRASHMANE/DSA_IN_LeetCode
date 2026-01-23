class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s1=Counter(s)
        s2=Counter(t)

        ans=''
        if len(s1) > len(s2):
            count = s1 - s2
        else:
            count = s2 - s1

        for i in count:
            for j in range(count[i]):
                ans+=i

        return ans
        