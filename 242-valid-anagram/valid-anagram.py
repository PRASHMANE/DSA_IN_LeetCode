class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False
        
        count = Counter(s)

        for i in t:
            if count.get(i,0) == 0:
                return False
            else:
                count[i]-=1
        
        return True