class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        n = len(s)
        i = 0
        res = 0

        while i < n:
            # first group
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            count1 = j - i

            # second group
            if j == n:
                break
            k = j
            while k < n and s[k] == s[j]:
                k += 1
            count2 = k - j

            res += min(count1, count2)
            i = j

        return res