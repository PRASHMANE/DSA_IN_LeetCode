from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        hsh = {}
        left = 0
        n = len(s)

        for right in range(n):
            hsh[s[right]] = hsh.get(s[right],0)+1

            while hsh.get(s[right]) > 1:
                hsh[s[left]]-=1
                if hsh[s[left]] == 0:
                    del hsh[s[left]]
                left+=1
            
            maxlen = max(maxlen,right-left+1)

        return maxlen