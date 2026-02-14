class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        hsh = {}
        for c in t:
            hsh[c] = hsh.get(c, 0) + 1

        left = 0
        count = 0
        minlen = float("inf")
        start = 0

        for right in range(len(s)):
            if s[right] in hsh:
                hsh[s[right]] -= 1
                if hsh[s[right]] >= 0:
                    count += 1

            while count == len(t):
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    start = left

                if s[left] in hsh:
                    hsh[s[left]] += 1
                    if hsh[s[left]] > 0:
                        count -= 1
                left += 1

        return "" if minlen == float("inf") else s[start:start + minlen]