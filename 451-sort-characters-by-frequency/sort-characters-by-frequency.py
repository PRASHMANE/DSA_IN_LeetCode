class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        count=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
        ans=""
        for i,j in count.items():
            while j > 0:
                ans+=i
                j-=1
        return ans
        