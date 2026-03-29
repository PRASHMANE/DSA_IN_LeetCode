class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        arr1 = []
        arr2 = []
        for i in s1:
            arr1.append(i)
        for i in s2:
            arr2.append(i)
        for i in range(4):
            for j in range(i+2,4):
                if j - i == 2:
                    if arr1[i] != arr2[i]:
                        arr2[i],arr2[j] = arr2[j],arr2[i]
        
        if s1 == "".join(arr2):
            return True
        return False
        