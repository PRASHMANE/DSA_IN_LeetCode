class Solution:
    def maxPower(self, s: str) -> int:
        maxlen=0
        left=0
        n=len(s)
        hsh={}
        for right in range(n):
            hsh[s[right]]=hsh.get(s[right],0)+1

            while len(hsh) > 1:
                hsh[s[left]] -= 1
                if hsh[s[left]] == 0:
                    del hsh[s[left]]
                left+=1
            
            if len(hsh) == 1:
                maxlen=max(maxlen,right-left+1)
        
        return maxlen
