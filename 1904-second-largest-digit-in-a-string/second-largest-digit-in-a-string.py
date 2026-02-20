class Solution:
    def secondHighest(self, s: str) -> int:
        ans=[]

        for ch in s:
            if ch.isdigit():
                ans.append(int(ch))
        ans= list(set(ans))

        n=len(ans)

        if n <= 1:
            return -1
        ans.sort()
        
        return ans[n-2]
