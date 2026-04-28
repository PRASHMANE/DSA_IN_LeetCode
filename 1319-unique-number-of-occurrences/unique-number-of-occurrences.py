class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count=Counter(arr)

        count2 = Counter([val for val in count.values()])

        for value in count2.values():
            if value > 1:
                return False
        return True