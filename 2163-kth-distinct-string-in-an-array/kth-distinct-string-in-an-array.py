class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp=Counter(arr)
        ans=""
        for ch in temp:
            if temp[ch] == 1 and k > 0:
                ans=ch
                k-=1
        if k > 0:
            return ""
        return ans