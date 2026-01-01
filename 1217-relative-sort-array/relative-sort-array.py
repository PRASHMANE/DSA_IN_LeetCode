from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Hash=Counter(arr1)
        ans=[]
        for i in arr2:
            ans.extend([i]*Hash[i])
            del Hash[i]
        for i in sorted(Hash.keys()):
            ans.extend([i]*Hash[i])
        return ans