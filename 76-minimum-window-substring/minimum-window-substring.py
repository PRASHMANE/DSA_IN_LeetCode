class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        minlen = float("inf")
        left=0
        m=len(t)
        n=len(s)
        count=0

        hsh={}

        for i in t:
            hsh[i]=hsh.get(i,0)+1

        for right in range(n):

            if s[right] in hsh:
                if hsh[s[right]] > 0:
                    count+=1
                hsh[s[right]]=hsh.get(s[right],0)-1

            while count == m:
                if right-left+1 < minlen:
                    minlen=right-left+1
                    start=left

                if s[left] in hsh:
                    hsh[s[left]]+=1

                    if hsh[s[left]] > 0:
                        count-=1
                left+=1
        return "" if minlen == float("inf") else s[start:start+minlen]


