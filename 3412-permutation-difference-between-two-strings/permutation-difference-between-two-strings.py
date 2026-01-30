class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        indices = [0]*26
        for i, ch in enumerate(s):
            indices[ord(ch)-97] = i
        
        ans = 0
        for i, ch in enumerate(t):
            ans += abs(indices[ord(ch)-97] - i)
        
        return ans
        