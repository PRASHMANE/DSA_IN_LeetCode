class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        window = defaultdict(int)
        left = 0
        distinct = 0
        ans = 0

        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == 1:
                distinct += 1

            if right - left + 1 > minSize:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    distinct -= 1
                left += 1

            if right - left + 1 == minSize and distinct <= maxLetters:
                sub = s[left:right + 1]
                freq[sub] += 1
                ans = max(ans, freq[sub])

        return ans