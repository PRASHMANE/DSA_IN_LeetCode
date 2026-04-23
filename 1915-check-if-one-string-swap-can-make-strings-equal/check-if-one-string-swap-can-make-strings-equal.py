class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        count =0
        for i , j in zip(s1,s2):
            if i != j:
                count+=1
        
        if count > 2 or "".join(sorted(s1)) != "".join(sorted(s2)):
            return False
        
        return True
        