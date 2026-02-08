from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        left=0
        n=len(s)
        hsh={}

        for right in range(n):
            if s[right] not in hsh or hsh[s[right]] < left:
                hsh[s[right]] = right
            else:
                left=hsh[s[right]]+1
                hsh[s[right]]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen

