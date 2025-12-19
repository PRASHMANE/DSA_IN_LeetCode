from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashtable=Counter(arr1)
        list1=[]
        for i in arr2:
            list1.extend([i]*hashtable[i])
        
        arr1.sort()
        for i in arr1:
            if i not in list1:
                list1.extend([i]*hashtable[i])
        return list1
        