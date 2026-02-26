class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        count1=Counter(target)
        count2=Counter(arr)

        for i in arr:
            if count1.get(i,0) != count2.get(i,0):
                return False
        return True