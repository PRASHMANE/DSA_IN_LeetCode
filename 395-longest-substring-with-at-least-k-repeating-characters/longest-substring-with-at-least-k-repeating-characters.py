class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0

        for target_unique in range(1, 27):
            freq = [0] * 26
            l = r = 0
            unique = count_k = 0

            while r < len(s):
                if freq[ord(s[r]) - 97] == 0:
                    unique += 1
                freq[ord(s[r]) - 97] += 1
                if freq[ord(s[r]) - 97] == k:
                    count_k += 1
                r += 1

                while unique > target_unique:
                    if freq[ord(s[l]) - 97] == k:
                        count_k -= 1
                    freq[ord(s[l]) - 97] -= 1
                    if freq[ord(s[l]) - 97] == 0:
                        unique -= 1
                    l += 1

                if unique == target_unique and unique == count_k:
                    ans = max(ans, r - l)

        return ans

        