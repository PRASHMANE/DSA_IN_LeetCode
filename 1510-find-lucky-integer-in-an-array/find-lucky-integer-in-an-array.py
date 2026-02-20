class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans=[]
        for key,value in count.items():
            if key == value:
                ans.append(key)
        
        if ans:
            return max(ans)
        return -1