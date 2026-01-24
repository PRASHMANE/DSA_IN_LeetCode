from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = defaultdict(lambda: -1)
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if last[ch] >= left:
                left = last[ch] + 1

            last[ch] = right
            ans = max(ans, right - left + 1)

        return ans