class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        hsh={}

        for i in candyType:
            hsh[i] = hsh.get(i,0)+1
        
        n=len(candyType)

        if len(hsh) >= n//2:
            return n//2
        
        return len(hsh)