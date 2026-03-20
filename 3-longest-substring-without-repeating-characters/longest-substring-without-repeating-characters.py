from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val=0
        left=0
        n=len(s)
        hsh=defaultdict(int)

        for right in range(n):
            hsh[s[right]]= hsh.get(s[right],0)+1

            while hsh[s[right]] > 1:
                hsh[s[left]]-=1
                if hsh[s[left]] == 0:
                    del hsh[s[left]]
                left+=1
        
            max_val = max(max_val,right-left+1)
        return max_val
