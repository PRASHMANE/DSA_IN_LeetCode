class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        rem = len(s) % k

        for i in range(0,len(s),k):
            ans.append(s[i:i+k])


        n=len(ans)-1
        if len(ans[n]) < k:
            for i in range(k-len(ans[n])):
                ans[n]+=fill

        return ans