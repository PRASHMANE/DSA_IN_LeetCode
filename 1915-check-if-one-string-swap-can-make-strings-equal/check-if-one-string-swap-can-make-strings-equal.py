class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        if len(s1) != len(s2):
            return Fasle

        if s1 == s2:
            return True

        for i in s2:
            if i not in s1:
                return False
        
        for i in s1:
            if i not in s2:
                return False
        for i in s1:
            if s1.count(i) != s2.count(i):
                return False


        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count+=1
                

        if count > 2 or count < 2:
            return False
        return True 
        