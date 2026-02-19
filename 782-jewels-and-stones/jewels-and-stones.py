class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        hsh={}

        for i in stones:
            hsh[i]=hsh.get(i,0)+1
        
        count=0
        for i in jewels:
            count+=hsh.get(i,0)
        
        return count