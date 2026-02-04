class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp=Counter(arr)
        ans=[]
        for ch in temp:
            if temp[ch] == 1:
                ans.append(ch)
        if len(ans) < k:
            return ""
        return ans[k-1]