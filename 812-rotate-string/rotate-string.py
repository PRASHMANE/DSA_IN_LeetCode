class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        cp=s
        for i in range(len(s)):
            if cp[i:] == goal:
                return True
            
            cp+=s[i]
        return False