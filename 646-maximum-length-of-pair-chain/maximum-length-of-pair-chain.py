class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key = lambda x:x[1])
        count = 0
        lastchain = float('-inf')

        for a,b in pairs:
            if a > lastchain:
                count+=1
                lastchain = b
        
        return count
