class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count=Counter(arr)

        ans=set()

        for val in count.values():
            if val in ans:
                return False
            ans.add(val)
        return True